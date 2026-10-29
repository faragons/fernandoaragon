---
layout: single
permalink: /
title: "Fernando M. Aragon"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% assign s = site.data.scholar %}

<p class="intro-lead">I am a Professor of Economics at Simon Fraser University (Canada). I received my PhD from the London School of Economics and joined the Department of Economics at SFU in 2010.</p>

My research relates to the fields of Development, Environmental, and Political Economics.

My work is applied and explores the role of natural resources and institutions on local development, economic effects of pollution, and adaptation to climate change, specially of rural households in less developed countries.

<div class="link-row">
  <a class="btn-formal" href="https://www.dropbox.com/s/ej31jr1ilo6gv2x/CV.doc?dl=0">CV</a>
  <a class="btn-formal" href="https://scholar.google.ca/citations?user=PqTDOgUAAAAJ&amp;hl=en">Google Scholar</a>
</div>

{% if s and s.citations %}
<div class="cites" aria-label="Google Scholar citation metrics">
  <p class="cites__title">Google Scholar citations</p>
  <div class="cites__grid">
    <div>
      <div class="cites__num">{{ s.citations_fmt | default: s.citations }}</div>
      <div class="cites__label">Citations</div>
      {% if s.citations_since %}<div class="cites__since">{{ s.citations_since_fmt | default: s.citations_since }} since {{ s.since_year }}</div>{% endif %}
    </div>
    <div>
      <div class="cites__num">{{ s.h_index }}</div>
      <div class="cites__label">h-index</div>
      {% if s.h_index_since %}<div class="cites__since">{{ s.h_index_since }} since {{ s.since_year }}</div>{% endif %}
    </div>
    <div>
      <div class="cites__num">{{ s.i10_index }}</div>
      <div class="cites__label">i10-index</div>
      {% if s.i10_index_since %}<div class="cites__since">{{ s.i10_index_since }} since {{ s.since_year }}</div>{% endif %}
    </div>
  </div>
  <p class="cites__note">Source: <a href="https://scholar.google.ca/citations?user=PqTDOgUAAAAJ&amp;hl=en">Google Scholar</a>. Updated {{ s.updated | date: "%B %-d, %Y" }}.</p>
</div>
{% endif %}

<div class="contact">
  <div>
    <p class="contact__label">Mailing address</p>
    <p>WMX 3635<br>Department of Economics<br>Simon Fraser University<br>Burnaby, BC, V5A 1S6<br>Canada</p>
  </div>
  <div>
    <p class="contact__label">Contact</p>
    <p>Phone: +1 778 782 9107<br>Email: <a href="mailto:faragons@sfu.ca">faragons@sfu.ca</a></p>
  </div>
</div>
