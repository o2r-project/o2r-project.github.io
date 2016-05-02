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

We use the kramdown parser engine and subsequently can use some advanced syntax (e.g. for named lists, image resizing, quotes, and more). See http://kramdown.gettalong.org/quickref.html.

*Note:* When the rendering engine changes, these changes are prone to break.

