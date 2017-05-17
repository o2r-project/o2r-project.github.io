---
layout: page
title: List of all blog posts
exclude_from_nav: true
---

{% for post in site.posts %}
  <ul>
    <li><a href="{{ site.url }}{{ post.url | remove: 'index.html' }}">{{ post.title }}</a> <span class="post-date">{{ post.date | date_to_string }}</span></li>
  </ul>
{% endfor %}