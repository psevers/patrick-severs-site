"""Seam + motion check for one loop. usage: python3 check-loop.py <letter>
Prints per-frame drift vs frame 0 (4 fps), the seam diff (last vs first), and writes a sheet in a fresh .loops/check/<letter>-*/ directory (still | first | peak | last).
Reject a clip when black ink changes (lines vanish, new figures appear) or the changed box spans the whole frame; the orange element alone should move."""
import sys, subprocess, pathlib, glob, tempfile
from PIL import Image, ImageChops, ImageStat
import os
if len(sys.argv) != 2 or sys.argv[1] not in tuple('abcdefghijkm'):
    raise SystemExit('usage: check-loop.py <plate letter: a-k or m>')
L = sys.argv[1]; REPO = pathlib.Path(__file__).resolve().parents[2]; LOOPS = pathlib.Path(os.environ.get('LOOP_OUT', REPO/'.loops'))
STILL = REPO/f'src/assets/images/plates/plate-{L}.jpg'
mp4 = LOOPS/f'plate-{L}.mp4'
if not STILL.is_file() or not mp4.is_file():
    raise SystemExit('Still image and loop MP4 must both exist')
check_dir = LOOPS/'check'; check_dir.mkdir(parents=True, exist_ok=True)
fdir = pathlib.Path(tempfile.mkdtemp(prefix=f'{L}-', dir=check_dir))
subprocess.run(['/opt/homebrew/bin/ffmpeg','-y','-loglevel','error','-i',str(mp4),'-vf','fps=4',str(fdir/'%03d.png')],check=True)
subprocess.run(['/opt/homebrew/bin/ffmpeg','-y','-loglevel','error','-sseof','-0.05','-i',str(mp4),'-update','1','-frames:v','1',str(fdir/'last.png')],check=True)
still = Image.open(STILL).convert('RGB'); sz = still.size
fr = [Image.open(f).convert('RGB').resize(sz) for f in sorted(glob.glob(str(fdir/'0*.png')))]
last = Image.open(fdir/'last.png').convert('RGB').resize(sz)
def d(a,b): return ImageChops.difference(a,b).convert('L')
def mean(im): return ImageStat.Stat(im).mean[0]
curve = [mean(d(f, fr[0])) for f in fr]
peak = max(range(len(fr)), key=lambda i: curve[i])
print('drift vs frame0 per 0.25s:', ' '.join(f'{c:.1f}' for c in curve))
print(f'peak motion frame {peak} mean {curve[peak]:.2f}; changed-bbox(>60):', d(fr[peak],fr[0]).point(lambda p:255 if p>60 else 0).getbbox())
print(f'seam last-vs-first mean {mean(d(last,fr[0])):.2f}   first-vs-still {mean(d(fr[0],still)):.2f}   last-vs-still {mean(d(last,still)):.2f}')
w,h = sz; sheet = Image.new('RGB',(w*2,h*2),'white')
for i,im in enumerate([still, fr[0], fr[peak], last]): sheet.paste(im,((i%2)*w,(i//2)*h))
out = fdir/'sheet.png'; sheet.resize((1400,int(1400*h*2/(w*2)))).save(out); print('sheet', out)
