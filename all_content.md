---
layout: no_menu
title: "Opening Reproducible Research: research project website and blog"
exclude_from_nav: true
---

![o2r logo](/public/images/logo-transparent.png)

# {{ page.title }}

{% capture authors %}{% for post in site.posts %}{% assign current_authors = post.author | split: ", " %}{% for author in current_authors %}{{ author }};{% endfor %}{% endfor %}{% endcapture %}

{% assign authors_array = authors | split: ";" | sort | uniq %}

**Blog post authors**:

<ul>
{% for author in authors_array %}
<li>{{ author }}</li>
{% endfor %}
</ul>


<div style="page-break-before: always !important;"></div>

## Blog posts

{% for post in site.posts %}

<div class="post">
<h3 class="post-title"><a href="{{ post.url | remove: 'index.html' }}">{{ post.title }}</a></h3>
<span class="post-date">{{ post.date | date_to_string }}{% if post.author %} | By {{ post.author }}{% endif %}</span>
{{ post.content | replace: 'h2', 'h4' | replace: 'h3', 'h5' }}
</div>

<div style="page-break-before: always !important;"></div>
{% endfor %}

## Website pages

{% for current_page in site.pages %}

{% if current_page.layout != redirect and current_page.exclude_from_nav != true and current_page.exclude_from_all_pages != true %}
<div class="page">
<h3 class="page-title">{{ current_page.title }}</h3>
{{ current_page.content | replace: 'h2', 'h4' | replace: 'h3', 'h5' }}
</div>

<div style="page-break-before: always !important;"></div>
{% endif %}

{% endfor %}
