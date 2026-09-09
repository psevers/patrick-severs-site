/* Risograph halftone treatment for images marked data-riso.
   Two ink screens (near-black and one spot colour) over paper, with a hair of
   misregistration that drifts with the pointer and a slow paper grain. WebGL 1,
   no library. Falls back to the plain image when WebGL is unavailable, and
   renders one still frame under prefers-reduced-motion. */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // plates: a small perspective tilt toward the pointer, and a sheen that follows it
  if (!reduced && window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('[data-tilt]').forEach(function (el) {
      el.addEventListener('pointermove', function (e) {
        var r = el.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
        el.style.setProperty('--px', px.toFixed(3)); el.style.setProperty('--py', py.toFixed(3));
        el.style.setProperty('--ry', ((px - 0.5) * 7).toFixed(2) + 'deg');
        el.style.setProperty('--rx', ((0.5 - py) * 7).toFixed(2) + 'deg');
      }, { passive: true });
      el.addEventListener('pointerleave', function () {
        el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg');
      });
    });
  }

  var imgs = document.querySelectorAll('img[data-riso]');
  if (!imgs.length) return;

  var VS = 'attribute vec2 a;varying vec2 v;void main(){v=a*0.5+0.5;gl_Position=vec4(a,0.,1.);}';
  var FS = [
    'precision mediump float;',
    'varying vec2 v;',
    'uniform sampler2D img;',
    'uniform vec2 res;',      // canvas size in px
    'uniform vec2 imgRes;',   // image size in px
    'uniform vec2 focus;',    // object-position, 0..1
    'uniform float zoom;',
    'uniform vec3 paper; uniform vec3 ink; uniform vec3 spot;',
    'uniform vec2 shift;',    // spot-plate misregistration in px
    'uniform float t;',
    'uniform float cell;',    // screen cell size in px
    'uniform float dark;',
    'uniform float mode;',    // 0 = halftone a photo, 1 = a plate already printed: misregister + grain only
    'float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}',
    'vec2 rot(vec2 p,float a){float c=cos(a),s=sin(a);return vec2(c*p.x-s*p.y,s*p.x+c*p.y);}',
    // coverage 0..1 -> dot mask at this pixel for a screen at angle a
    'float screen(vec2 px,float a,float k){vec2 p=rot(px,a)/cell;vec2 f=fract(p)-0.5;float d=length(f)*2.0;float r=sqrt(clamp(k,0.0,1.0))*0.98;return 1.0-smoothstep(r-0.18,r+0.04,d);}',
    'vec2 coverUV(vec2 uv){float ca=res.x/res.y,ia=imgRes.x/imgRes.y;vec2 s=vec2(1.0);if(ca>ia){s.y=ia/ca;}else{s.x=ca/ia;}s/=zoom;return focus+(uv-focus)*s;}',
    'vec3 tex(vec2 uv){return texture2D(img,vec2(uv.x,1.0-uv.y)).rgb;}',
    'float lum(vec2 uv){return dot(tex(uv),vec3(0.299,0.587,0.114));}',
    'void main(){',
    '  vec2 px=v*res;',
    '  vec2 uv=coverUV(v);',
    '  float g=hash(floor(px*0.5)+floor(t*6.0));',        // coarse, slowly ticking grain
    '  if(mode>0.5){',
    '    vec3 c=tex(uv); vec3 cs=tex(coverUV(v+shift/res*0.3));',
    '    vec3 col=vec3(cs.r,c.g,c.b)+(g-0.5)*0.045;',       // the spot plate sits a hair off register
    '    if(dark>0.5){col*=0.94;}',
    '    gl_FragColor=vec4(col,1.0);return;',
    '  }',
    '  float paperGrain=(hash(floor(px*0.25))-0.5)*0.05;',
    '  float L=lum(uv)+(g-0.5)*0.10;',
    '  L=smoothstep(0.08,0.95,L);',                        // lift contrast, keep highlights paper
    '  vec2 uv2=coverUV(v+shift/res);',
    '  float L2=lum(uv2)+(g-0.5)*0.08;',
    '  float kInk=pow(1.0-L,1.7);',                        // shadows
    '  float kSpot=smoothstep(0.10,0.80,1.0-L2)*0.85;',    // midtones
    '  float dInk=screen(px,0.785,kInk);',
    '  float dSpot=screen(px+vec2(0.0,cell*0.5),0.26,kSpot);',
    '  vec3 col=paper+paperGrain;',
    '  if(dark>0.5){',
    // dark paper: the spot plate prints as a tint, the light ink as the image
    '    col=mix(col,mix(col,spot,0.55),dSpot*0.9);',
    '    col=mix(col,ink,dInk);',
    '  }else{',
    '    col=mix(col,col*spot/max(paper,vec3(0.001)),dSpot);',
    '    col=mix(col,ink,dInk);',
    '  }',
    '  gl_FragColor=vec4(col,1.0);',
    '}'
  ].join('\n');

  function cssColor(name) {
    var s = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    var m = s.match(/^#([0-9a-f]{6})$/i);
    if (!m) return [0.5, 0.5, 0.5];
    var n = parseInt(m[1], 16);
    return [(n >> 16 & 255) / 255, (n >> 8 & 255) / 255, (n & 255) / 255];
  }
  function isDark() {
    var t = document.documentElement.getAttribute('data-theme');
    return t ? t === 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  function mount(img) {
    var host = img.parentElement;
    var canvas = document.createElement('canvas');
    canvas.className = 'riso-canvas';
    canvas.setAttribute('aria-hidden', 'true');
    var gl = canvas.getContext('webgl', { antialias: false, alpha: false, premultipliedAlpha: false });
    if (!gl) return;
    function sh(type, src) { var s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) { console.error('riso shader:', gl.getShaderInfoLog(s)); return null; } return s; }
    var vs = sh(gl.VERTEX_SHADER, VS), fs = sh(gl.FRAGMENT_SHADER, FS);
    if (!vs || !fs) return;
    var prog = gl.createProgram(); gl.attachShader(prog, vs); gl.attachShader(prog, fs); gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
      console.error('riso program:', gl.getProgramInfoLog(prog));
      gl.deleteProgram(prog);
      return;
    }
    gl.useProgram(prog);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
    var a = gl.getAttribLocation(prog, 'a'); gl.enableVertexAttribArray(a); gl.vertexAttribPointer(a, 2, gl.FLOAT, false, 0, 0);
    var U = {}; ['img', 'res', 'imgRes', 'focus', 'zoom', 'paper', 'ink', 'spot', 'shift', 't', 'cell', 'dark', 'mode'].forEach(function (n) { U[n] = gl.getUniformLocation(prog, n); });

    var tex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, img);
    gl.uniform1i(U.img, 0);
    gl.uniform2f(U.imgRes, img.naturalWidth, img.naturalHeight);
    var fp = (img.dataset.focus || '0.5 0.5').split(/\s+/).map(Number);
    gl.uniform2f(U.focus, fp[0], 1 - fp[1]);
    gl.uniform1f(U.zoom, parseFloat(img.dataset.zoom || '1'));
    gl.uniform1f(U.mode, img.dataset.riso === 'plate' ? 1 : 0);

    var contextLost = false;
    canvas.addEventListener('webglcontextlost', function () {
      contextLost = true;
      if (raf) cancelAnimationFrame(raf);
      raf = 0;
      host.classList.remove('riso-on');
      canvas.remove();
    });
    host.appendChild(canvas);
    host.classList.add('riso-on');

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = 0, h = 0;
    function size() {
      if (contextLost) return;
      var r = host.getBoundingClientRect();
      w = Math.max(1, Math.round(r.width * dpr)); h = Math.max(1, Math.round(r.height * dpr));
      if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; gl.viewport(0, 0, w, h); }
      gl.uniform2f(U.res, w, h);
      gl.uniform1f(U.cell, parseFloat(img.dataset.cell || '3.2') * dpr);
    }
    function colors() {
      if (contextLost) return;
      var p = cssColor('--paper'), k = cssColor('--ink'), s = cssColor('--spot');
      gl.uniform3f(U.paper, p[0], p[1], p[2]); gl.uniform3f(U.ink, k[0], k[1], k[2]); gl.uniform3f(U.spot, s[0], s[1], s[2]);
      gl.uniform1f(U.dark, isDark() ? 1 : 0);
    }
    var mx = 0, my = 0, tx = 0, ty = 0, start = performance.now(), raf = 0, visible = true;
    function draw(now) {
      if (contextLost) return;
      raf = 0;
      mx += (tx - mx) * 0.08; my += (ty - my) * 0.08;
      gl.uniform2f(U.shift, (2.2 + mx * 4.0) * dpr, (1.2 + my * 3.0) * dpr);
      gl.uniform1f(U.t, reduced ? 0 : (now - start) / 1000);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
      if (!reduced && visible) raf = requestAnimationFrame(draw);
    }
    function kick() { if (!contextLost && !raf) raf = requestAnimationFrame(draw); }

    size(); colors(); kick();
    window.addEventListener('resize', function () { size(); kick(); });
    new MutationObserver(function () { colors(); kick(); }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () { colors(); kick(); });
    if (!reduced) {
      window.addEventListener('pointermove', function (e) {
        tx = (e.clientX / window.innerWidth - 0.5); ty = (e.clientY / window.innerHeight - 0.5); kick();
      }, { passive: true });
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(function (en) { visible = en[0].isIntersecting; if (visible) kick(); }).observe(host);
      }
    }
  }

  imgs.forEach(function (img) {
    if (img.complete && img.naturalWidth) mount(img);
    else img.addEventListener('load', function () { mount(img); }, { once: true });
  });
})();
