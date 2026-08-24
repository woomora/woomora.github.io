---
title: Photography
layout: template
filename: photo
order: 5
---

<style>
  .pgrid{columns:2;column-gap:14px}
  .pitem{display:block;width:100%;margin:0 0 14px;padding:0;border:1px solid var(--border);
         background:var(--card);border-radius:2px;overflow:hidden;cursor:zoom-in;
         break-inside:avoid;position:relative;font:inherit;color:inherit}
  .pitem img{display:block;width:100%;height:auto}
  .pitem__cap{position:absolute;left:0;right:0;bottom:0;padding:22px 10px 8px;text-align:left;
              font-family:var(--mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;
              color:#fff;background:linear-gradient(transparent,rgba(20,18,17,.72));
              opacity:0;transition:opacity .25s ease}
  .pitem:hover .pitem__cap,.pitem:focus-visible .pitem__cap{opacity:1}
  @media (max-width:640px){.pgrid{columns:1}.pitem__cap{opacity:1}}

  .lb[hidden]{display:none}
  .lb{position:fixed;inset:0;z-index:50;background:rgba(18,16,15,.94);
      display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:28px}
  .lb__img{max-width:min(1200px,92vw);max-height:78vh;object-fit:contain;display:block;
           border-radius:2px;background:#26221f}
  .lb__bar{display:flex;align-items:center;gap:16px;font-family:var(--mono);font-size:10.5px;
           letter-spacing:.1em;text-transform:uppercase;color:#cfc7bf}
  .lb__count{color:#8d857d}
  .lb button{background:none;border:0;padding:9px;cursor:pointer;color:#cfc7bf;
             border-radius:3px;display:inline-flex;line-height:0}
  .lb button:hover{color:#fff;background:rgba(255,255,255,.09)}
  .lb button:focus-visible{outline:2px solid #fff;outline-offset:2px}
  .lb__close{position:absolute;top:18px;right:18px}
  .lb__nav{position:absolute;top:50%;transform:translateY(-50%)}
  .lb__prev{left:14px}.lb__next{right:14px}
  @media (prefers-reduced-motion:reduce){.pitem__cap{transition:none}}
</style>

<div class="card page">
  <div class="pgrid" id="pgrid">
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/dejarse_caer.jpg' | relative_url }}" data-cap="Dejarse caer"><img src="{{ '/images/photo portfolio/thumbs/dejarse_caer.jpg' | relative_url }}" alt="Dejarse caer" loading="lazy"><span class="pitem__cap">Dejarse caer</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/salineras_maras.jpg' | relative_url }}" data-cap="Salineras de Maras"><img src="{{ '/images/photo portfolio/thumbs/salineras_maras.jpg' | relative_url }}" alt="Salineras de Maras" loading="lazy"><span class="pitem__cap">Salineras de Maras</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/ciego_tabasco.jpg' | relative_url }}" data-cap="Ciego, Tabasco"><img src="{{ '/images/photo portfolio/thumbs/ciego_tabasco.jpg' | relative_url }}" alt="Ciego, Tabasco" loading="lazy"><span class="pitem__cap">Ciego, Tabasco</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/sacre_caeur.jpg' | relative_url }}" data-cap="Sacré-Cœur"><img src="{{ '/images/photo portfolio/thumbs/sacre_caeur.jpg' | relative_url }}" alt="Sacré-Cœur" loading="lazy"><span class="pitem__cap">Sacré-Cœur</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/whatever_it_takes.jpg' | relative_url }}" data-cap="Whatever it takes"><img src="{{ '/images/photo portfolio/thumbs/whatever_it_takes.jpg' | relative_url }}" alt="Whatever it takes" loading="lazy"><span class="pitem__cap">Whatever it takes</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/zocalo.jpg' | relative_url }}" data-cap="Zócalo"><img src="{{ '/images/photo portfolio/thumbs/zocalo.jpg' | relative_url }}" alt="Zócalo" loading="lazy"><span class="pitem__cap">Zócalo</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/vinicunca.jpg' | relative_url }}" data-cap="Vinicunca"><img src="{{ '/images/photo portfolio/thumbs/vinicunca.jpg' | relative_url }}" alt="Vinicunca" loading="lazy"><span class="pitem__cap">Vinicunca</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/memoria.jpg' | relative_url }}" data-cap="Memoria"><img src="{{ '/images/photo portfolio/thumbs/memoria.jpg' | relative_url }}" alt="Memoria" loading="lazy"><span class="pitem__cap">Memoria</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/pompidou.jpg' | relative_url }}" data-cap="Pompidou"><img src="{{ '/images/photo portfolio/thumbs/pompidou.jpg' | relative_url }}" alt="Pompidou" loading="lazy"><span class="pitem__cap">Pompidou</span></button>
    <button class="pitem" data-full="{{ '/images/photo portfolio/large/ninos_caracol.jpg' | relative_url }}" data-cap="Niños, Caracol"><img src="{{ '/images/photo portfolio/thumbs/ninos_caracol.jpg' | relative_url }}" alt="Niños, Caracol" loading="lazy"><span class="pitem__cap">Niños, Caracol</span></button>
  </div>
</div>

<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Photograph viewer">
  <button class="lb__close" id="lbClose" aria-label="Close">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
  </button>
  <button class="lb__nav lb__prev" id="lbPrev" aria-label="Previous photograph">
    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>
  </button>
  <img class="lb__img" id="lbImg" alt="">
  <button class="lb__nav lb__next" id="lbNext" aria-label="Next photograph">
    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>
  </button>
  <div class="lb__bar"><span id="lbCap"></span><span class="lb__count" id="lbCount"></span></div>
</div>

<script>
(function(){
  var items = [].slice.call(document.querySelectorAll('#pgrid .pitem'));
  if (!items.length) return;
  var lb = document.getElementById('lb'), img = document.getElementById('lbImg'),
      cap = document.getElementById('lbCap'), count = document.getElementById('lbCount'),
      closeBtn = document.getElementById('lbClose'),
      prevBtn = document.getElementById('lbPrev'), nextBtn = document.getElementById('lbNext');
  var i = 0, opener = null;

  function show(n){
    i = (n + items.length) % items.length;
    var el = items[i];
    img.src = el.getAttribute('data-full');
    img.alt = el.getAttribute('data-cap');
    cap.textContent = el.getAttribute('data-cap');
    count.textContent = (i + 1) + ' / ' + items.length;
  }
  function open(n){
    opener = items[n];
    show(n);
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }
  function close(){
    lb.hidden = true;
    img.removeAttribute('src');
    document.body.style.overflow = '';
    if (opener) opener.focus();
  }

  items.forEach(function(el, n){ el.addEventListener('click', function(){ open(n); }); });
  closeBtn.addEventListener('click', close);
  prevBtn.addEventListener('click', function(){ show(i - 1); });
  nextBtn.addEventListener('click', function(){ show(i + 1); });
  lb.addEventListener('click', function(e){ if (e.target === lb) close(); });
  document.addEventListener('keydown', function(e){
    if (lb.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(i - 1);
    else if (e.key === 'ArrowRight') show(i + 1);
  });
})();
</script>
