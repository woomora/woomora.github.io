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
  @media (max-width:640px){.pgrid{columns:1}}

</style>

<div class="page">
  <div class="pgrid" id="pgrid">
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/dejarse_caer.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/dejarse_caer.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/salineras_maras.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/salineras_maras.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/ciego_tabasco.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/ciego_tabasco.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/sacre_caeur.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/sacre_caeur.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/whatever_it_takes.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/whatever_it_takes.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/zocalo.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/zocalo.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/vinicunca.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/vinicunca.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/memoria.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/memoria.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/pompidou.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/pompidou.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
    <button class="pitem" data-lb="{{ '/images/photo portfolio/large/ninos_caracol.jpg' | relative_url }}"><img src="{{ '/images/photo portfolio/thumbs/ninos_caracol.jpg' | relative_url }}" alt="Photograph" loading="lazy"></button>
  </div>
</div>
