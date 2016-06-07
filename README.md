# o2r

This is the project website of the DFG-funded research project "Opening Reproducible Research" by Institute for Geoinformatics (ifgi) and University and Regional Library (ULB), University of Münster, Germany

The design is base on [Hyde](https://github.com/poole/hyde) by Mark Otto.

## Building the site

Follow the [instructions](https://github.com/poole/poole) for Poole to install the required software. Then run the site locally with

```
bundle exec jekyll serve
```

Use the `--draft` [switch](https://jekyllrb.com/docs/drafts/) to preview the draft posts.

## Site testing

[![Build Status](https://travis-ci.org/o2r-project/o2r-project.github.io.svg?branch=master)](https://travis-ci.org/o2r-project/o2r-project.github.io)

The page is tested in the context of a Travis CI build: https://travis-ci.org/o2r-project/o2r-project.github.io

This is based on the files `.travis.yml` and `Gemfile`.

## Useful stuff

### Images

We use the kramdown parser engine and subsequently can use some advanced syntax (e.g. for named lists, image resizing, quotes, and more). See http://kramdown.gettalong.org/quickref.html.

*Note:* When the rendering engine changes, these changes are prone to break.

### Excerpts

The file `index.html` contains some logic trying to to a clever handling of the post excerpts, i.e. the texts that are shown in the listing of posts. The procedure is as follows:

- If the `disable_excerpt` attribute is set to `true`, show the full content and do not show the "Read more" link. This is useful for short posts.
- If the number of paragraphs in the post's excerpt is the same as the number of paragraphs of the post content, then see above. This is so that no "Read more" link is put on pages with no further text.
- In any other case, show the excerpt and add a "Read more" link. You can set the length of the excerpt manually by using Jekyll's default tag `<!--more-->`.

### Comments

We use [DISQUS]() for comments, based on their [Jekyll Installation Instructions](), though not quite: Instead of enabling comments for each post, you must add  `disable_comments: true` to the frontmatter to disable them explicitly.