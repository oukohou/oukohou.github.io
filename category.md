---
layout: page
title: 分类
permalink: /category/
---

<div class="category">
  <h1>文章分类</h1>

  <ul id="categories">
  {% for category in site.categories %}
    <li><a href="{{ site.baseurl }}/category/#{{ category | first }}">{{ category | first }}({{ category | last | size }})</a></li>
  {% endfor %}
  </ul>

  <div class="post post-archive">
  {% for category in site.categories %}
  <h3 id="{{ category | first }}">{{ category | first }}</h3>
  <ul class="arc-list">
      {% for post in category.last %}
          <li><span class="date">{{ post.date | date: "%B %e, %Y" }}</span><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endfor %}
  </ul>
  {% endfor %}
  </div>
</div>
