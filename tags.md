---
layout: page
title: 标签
permalink: /tags/
---

<div id="tags">
  <ul id="label_box">
  {% for tag in site.tags %}
    <li><a href="{{ site.baseurl }}/tags/#{{ tag[0] }}">{{ tag[0] }} <span>{{ tag | last | size }}</span></a></li>
  {% endfor %}
  </ul>

  <div class="post post-archive">
  {% for tag in site.tags %}
  <h3 id="{{ tag | first }}">{{ tag | first }}</h3>
  <ul>
      {% for post in tag.last %}
          <li><span class="date">{{ post.date | date: "%B %e, %Y" }}</span><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>
      {% endfor %}
  </ul>
  {% endfor %}
  </div>
</div>
