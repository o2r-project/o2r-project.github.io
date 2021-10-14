---
layout: page
title: 📑 Blogroll
description: "Blogroll of the project Opening Reproducible Research: Docker, R, and reproducible research"
exclude_from_all_pages: true
no_citation: true
---

<div class="posts">
  {% for post in paginator.posts %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <span class="post-date">{{ post.date | date_to_string }}{% if post.author %} | {{ post.author }}{% endif %}</span>
    
    {% assign total_paragraphs = post.content | split: '<p>' | size | minus: 1 %}
    {% assign excerpt_paragraphs = post.excerpt | split: '<p>' | size | minus: 1 %}
    
    {% if post.disable_excerpt or total_paragraphs == excerpt_paragraphs %}
      {{ post.content }}
    {% else %}
      {% if post.content contains '<!--more-->' %}
        {% comment %}
        {% when more is set manually, we might have more paragraphs, so remove the last closing p tag, add the three dots, then close the p tag %}
        {% endcomment %}
        {{ post.content | split: '<!--more-->' | first | rstrip | append: '@END@' | remove: '</p>@END@' | remove: '@END@' }}<a href="{{ post.url }}">&hellip;</a></p>
      {% else %}
        <p>
          {{ post.excerpt | remove: '<p>' | remove: '</p>' | rstrip | append: '@END@' | remove: '.@END@' }}<a href="{{ post.url }}">&hellip;</a>
        </p>
        
        {% comment %}
        {% consider linking to anchor for read more, see http://www.seanbuscay.com/blog/jekyll-teaser-pager-and-read-more/ %}
        {% endcomment %}
      {% endif %}
      
      <p><strong><a href="{{ post.url }}">read more&hellip;</a></strong></p>
    {% endif %}
  </div>
  {% endfor %}
</div>

<div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ site.baseurl | absolute_url }}page{{paginator.next_page}}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ site.baseurl | absolute_url }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.baseurl | absolute_url }}page{{paginator.previous_page}}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div>
