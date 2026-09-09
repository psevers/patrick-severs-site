"""Turn one riso plate into a short seamless loop via fal.ai (Kling v3 pro), then encode for the site.
usage: NOEND=1 python3 fal-loop.py <plate letter> [kling|ltx] [seconds]   # paid call; ask first
       PP=4  python3 fal-loop.py encode <plate letter> [model]           # re-encode a downloaded raw clip, free
Recipe that works (2026-09-09): no end frame (NOEND=1; sending the still as both start and end froze the clip),
one explicit motion line per plate (MOTION), cfg 0.75, then trim to 4 s and ping-pong (PP=4) so the loop
returns to frame one. Reads FAL_KEY from the repo's .env.local and never prints it."""
import sys, os, json, time, base64, urllib.request, urllib.error, subprocess, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(os.environ.get('LOOP_OUT', REPO / '.loops'))  # gitignored; install the good ones into src/assets/video by hand
FFMPEG = pathlib.Path('/opt/homebrew/bin/ffmpeg')  # Homebrew ffmpeg 8; the playwright build has no h264 or vp9 encoder
MODELS = {
    # start and end image are the same still, so the clip returns to its first frame and loops without a seam
    'ltx':   ('lightricks/ltx-2.5/image-to-video/fast', lambda uri, d, L: {'image_url': uri, 'end_image_url': uri, 'prompt': prompt(L), 'duration': d, 'resolution': '1080p', 'aspect_ratio': '16:9', 'fps': 24, 'generate_audio': False, 'camera_motion': 'static'}),
    'kling': ('fal-ai/kling-video/v3/pro/image-to-video',  lambda uri, d, L: {'start_image_url': uri, 'end_image_url': uri, 'prompt': prompt(L), 'duration': str(d), 'generate_audio': False, 'negative_prompt': 'camera movement, zoom, pan, new objects, text, colour change, blur, distort', 'cfg_scale': 0.75}),
}
BASE = ('A two-colour risograph print on cream paper, flat black ink and one orange element. Locked-off camera, perfectly still. '
        'The paper and every black shape stay exactly in place. The only motion in the whole frame: {motion} '
        'The movement is clear and readable but gentle, one slow cycle, and the orange element ends exactly where it started. '
        'No new objects, no text, no colour change, no zoom, no pan, no lighting change.')
MOTION = {
    'a': 'a slow ripple travels along the orange channels from left to right, like water flowing, while every thin black contour line stays printed exactly as it is, none fade or vanish.',
    'b': 'the orange building block hanging from the crane cable swings side to side a few degrees, like a pendulum, then settles back to centre.',
    'c': 'the orange paper boat rocks gently and drifts a little across the desk, then returns to its spot.',
    'd': 'the orange chair scoots out from the round table a little, pauses, and slides back into place.',
    'e': 'the orange cable holding the chairs bows and sways gently, the chairs bobbing with it, then settles.',
    'f': 'the orange figure in the aisle takes one slow step forward and steps back; the seated black crowd is fixed printed ink and does not change, no faces or hats appear, no seat moves.',
    'g': 'the orange tile slides forward one slot along the belt and slides back; the belt, the black tiles and the four black gate frames stay printed exactly as they are, nothing vanishes.',
    'h': 'the orange tent flaps ripple in a light breeze and settle.',
    'i': 'the orange awning over the shop door billows and flaps in a light breeze, then goes still.',
    'j': 'the orange baton in the conductor\'s hand sweeps through one slow beat and returns to its raised position.',
    'k': 'the orange hub circle pulses gently larger and smaller like a slow heartbeat, staying in place; the black spokes and the seven black squares are fixed printed ink and do not move or rotate.',
    'm': 'the orange flag at the top of the staircase waves in a light breeze and settles.',
}
def prompt(letter): return BASE.format(motion=MOTION[letter])

def key():
    for line in (REPO / '.env.local').read_text().splitlines():
        if line.startswith('FAL_KEY=') and len(line) > 8:
            return line[8:].strip()
    sys.exit('FAL_KEY missing in .env.local')

def call(url, method='GET', body=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body else None,
                                 headers={'Authorization': 'Key ' + key(), 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f'fal HTTP {e.code}: {e.read()[:500].decode(errors="replace")}')

def main():
    letter = sys.argv[1]; model = sys.argv[2] if len(sys.argv) > 2 else 'ltx'; dur = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    mid, build = MODELS[model]
    noend = os.environ.get('NOEND') == '1'
    src = REPO / f'src/assets/images/plates/plate-{letter}.jpg'
    uri = 'data:image/jpeg;base64,' + base64.b64encode(src.read_bytes()).decode()
    OUT.mkdir(exist_ok=True)
    body = build(uri, dur, letter)
    if noend: body.pop('end_image_url', None)
    sub = call(f'https://queue.fal.run/{mid}', 'POST', body)
    rid = sub['request_id']; print('submitted', rid)
    while True:
        st = call(sub['status_url'] + '?logs=0')
        print(' ', st['status'], st.get('queue_position', ''))
        if st['status'] == 'COMPLETED': break
        time.sleep(5)
    res = call(sub['response_url'])
    vurl = res['video']['url']
    raw = OUT / f'plate-{letter}-{model}-raw.mp4'
    urllib.request.urlretrieve(vurl, raw); print('downloaded', raw, raw.stat().st_size)
    encode(letter, raw)

def encode(letter, raw, trim=None):
    """h264 + webm at 1400 wide, no audio. PP=<seconds> env: keep the first N seconds and append them reversed,
    so the clip returns to frame one (for pendulum-style motion this reads as a natural back-swing)."""
    trim = trim or os.environ.get('PP')
    vf = 'scale=1400:-2'
    if trim:
        vf = f'trim=0:{trim},setpts=PTS-STARTPTS,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,{vf}'
    for ext, args in (('mp4', ['-c:v', 'libx264', '-crf', '26', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart']),
                      ('webm', ['-c:v', 'libvpx-vp9', '-crf', '38', '-b:v', '0', '-row-mt', '1'])):
        dst = OUT / f'plate-{letter}.{ext}'
        subprocess.run([str(FFMPEG), '-y', '-loglevel', 'error', '-i', str(raw), '-an', '-filter_complex' if trim else '-vf', vf, *args, str(dst)], check=True)
        print(dst.name, dst.stat().st_size // 1024, 'KB')

if __name__ == '__main__':
    if sys.argv[1] == 'encode': encode(sys.argv[2], OUT / f'plate-{sys.argv[2]}-{sys.argv[3] if len(sys.argv)>3 else "kling"}-raw.mp4')
    else: main()
