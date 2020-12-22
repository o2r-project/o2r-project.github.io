# o2r

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1485438.svg)](https://doi.org/10.5281/zenodo.1485438)

This is the project website of the DFG-funded research project "Opening Reproducible Research" by Institute for Geoinformatics (ifgi) and University and Regional Library (ULB), University of Münster, Germany

The design is based on [Hyde](https://github.com/poole/hyde) by Mark Otto.

## Building the site

Follow the [instructions](https://github.com/poole/poole) for Poole to install the required software.
Then run the site locally with

```
bundle exec jekyll serve
```

Use the `--draft` [switch](https://jekyllrb.com/docs/drafts/) to preview the draft posts.

## Publishing site repository and PDF on Zenodo

After each new blog post is published, a [Zenodo deposit](https://doi.org/10.5281/zenodo.1485437) (first deposit `https://zenodo.org/record/1485438`) with a PDF of all blog posts and relevant pages is updated automatically using a GitHub action, see `Makefile` and `.github/workflows/deposit.yml` for details.
For the automatic deployment, a Zenodo token with write access to the deposit above must be stored as a [Repository secret](https://github.com/o2r-project/o2r-project.github.io/settings/secrets/actions).
_NOTE:_ Make sure to disable the workflow on forks.

The PDF file `o2r_project_website_and_blog.pdf` is generated from a special page at [http://127.0.0.1:4000/all_content/](http://127.0.0.1:4000/all_content/) (file `all_content.md`) using [`wkhtmltopdf`](https://wkhtmltopdf.org/).
An archive of the current repository `HEAD` is zipped into `o2r_project_website_and_blog_git-repository.zip`.

Both these files are then published to Zenodo with the [Zenodo API](http://developers.zenodo.org/) by the file `zenodo_release.py`.
The environment variable `ZENODO_TOKEN` must have a valid API key for Zenodo (or for Zenodo Sandbox for testing).

The process is controlled with the make target `update_zenodo_deposit` or directly with

```bash
ZENODO_TOKEN=... python3 zenodo_release.py
# increase logging output for testing with LOGLEVEL=DEBUG
```

## Site testing

[![Build Status](https://travis-ci.org/o2r-project/o2r-project.github.io.svg?branch=master)](https://travis-ci.org/o2r-project/o2r-project.github.io)

The page is tested in the context of a Travis CI build: https://travis-ci.org/o2r-project/o2r-project.github.io

This is based on the files `.travis.yml` and `Gemfile`.

## Useful stuff

### Authoring posts & publishing drafts

You can use [jekyll-compose](https://github.com/jekyll/jekyll-compose) to streamline some tasks, e.g.

```bash
bundle exec jekyll draft "My new draft"
bundle exec jekyll publish _drafts/my-new-draft.md
```

### Images

We use the kramdown parser engine and subsequently can use some [advanced syntax](http://kramdown.gettalong.org/syntax.html) (e.g. for named lists, [image resizing](http://kramdown.gettalong.org/syntax.html#images), quotes, and more).

To float images, use the CSS classes `.img.leftfloat` or `.img.rightfloat`, for example `![geocontainers logo](http://geocontainers.org/img/geocontainers-logo.png "geocontainers logo"){:width="100" .img.rightfloat}`

*Note:* When the rendering engine is changed, these changes are prone to break.

### Excerpts

The file `index.html` contains some logic trying to do a clever handling of the post excerpts, i.e. the texts that are shown in the listing of posts. The procedure is as follows:

- If the `disable_excerpt` attribute is set to `true`, show the full content and do not show the "Read more" link. This is useful for short posts.
- If the number of paragraphs in the post's excerpt is the same as the number of paragraphs of the post content, then see above. This is so that no "Read more" link is put on pages with no further text.
- In any other case, show the excerpt and add a "Read more" link. You can set the length of the excerpt manually by using Jekyll's default tag `<!--more-->`.

### Ribbon

A generic "Fork me" ribbon has been added and can be configured (text, link) in the file `_config.yml`. The color is configured in `public/css/o2r.css`. The ribbon appears on all pages via `_layouts/default.html`, and stylesheets are included in `_includes/head_default.html` if enabled.

### Exclude pages from menu

If you do not want a page to appear in the left hand side menu, include the parameter `exclude_from_nav: true` in the page's frontmatter.

### Footnotes

```
Testing footnotes[^2] for *Opening Reproducible Research*[^1].

[^1]: would be useful!
[^2]: yes, no promises on results...
```

## License

Except where otherwise noted site content created by the o2r project in this repository is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
