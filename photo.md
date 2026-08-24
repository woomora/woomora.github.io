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

  @media (prefers-reduced-motion:reduce){.pitem__cap{transition:none}}
</style>

<div class="card page">
  <div class="pgrid" id="pgrid">
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/dejarse_caer.jpg' | relative_url }}" data-lb-cap="Dejarse caer"><img src="{{ '/images/photo portfolio/thumbs/dejarse_caer.jpg' | relative_url }}" alt="Dejarse caer" loading="lazy"><span class="pitem__cap">Dejarse caer</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/salineras_maras.jpg' | relative_url }}" data-lb-cap="Salineras de Maras"><img src="{{ '/images/photo portfolio/thumbs/salineras_maras.jpg' | relative_url }}" alt="Salineras de Maras" loading="lazy"><span class="pitem__cap">Salineras de Maras</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/ciego_tabasco.jpg' | relative_url }}" data-lb-cap="Ciego, Tabasco"><img src="{{ '/images/photo portfolio/thumbs/ciego_tabasco.jpg' | relative_url }}" alt="Ciego, Tabasco" loading="lazy"><span class="pitem__cap">Ciego, Tabasco</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/sacre_caeur.jpg' | relative_url }}" data-lb-cap="Sacré-Cœur"><img src="{{ '/images/photo portfolio/thumbs/sacre_caeur.jpg' | relative_url }}" alt="Sacré-Cœur" loading="lazy"><span class="pitem__cap">Sacré-Cœur</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/whatever_it_takes.jpg' | relative_url }}" data-lb-cap="Whatever it takes"><img src="{{ '/images/photo portfolio/thumbs/whatever_it_takes.jpg' | relative_url }}" alt="Whatever it takes" loading="lazy"><span class="pitem__cap">Whatever it takes</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/zocalo.jpg' | relative_url }}" data-lb-cap="Zócalo"><img src="{{ '/images/photo portfolio/thumbs/zocalo.jpg' | relative_url }}" alt="Zócalo" loading="lazy"><span class="pitem__cap">Zócalo</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/vinicunca.jpg' | relative_url }}" data-lb-cap="Vinicunca"><img src="{{ '/images/photo portfolio/thumbs/vinicunca.jpg' | relative_url }}" alt="Vinicunca" loading="lazy"><span class="pitem__cap">Vinicunca</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/memoria.jpg' | relative_url }}" data-lb-cap="Memoria"><img src="{{ '/images/photo portfolio/thumbs/memoria.jpg' | relative_url }}" alt="Memoria" loading="lazy"><span class="pitem__cap">Memoria</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/pompidou.jpg' | relative_url }}" data-lb-cap="Pompidou"><img src="{{ '/images/photo portfolio/thumbs/pompidou.jpg' | relative_url }}" alt="Pompidou" loading="lazy"><span class="pitem__cap">Pompidou</span></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/ninos_caracol.jpg' | relative_url }}" data-lb-cap="Niños, Caracol"><img src="{{ '/images/photo portfolio/thumbs/ninos_caracol.jpg' | relative_url }}" alt="Niños, Caracol" loading="lazy"><span class="pitem__cap">Niños, Caracol</span></button>
  </div>
</div>
