---
layout: post
title: "Archiving a Research Project Website on Zenodo"
categories:
  - "blogging"
  - "publishing"
  - "preservation"
  - "archival"
  - "website"
  - "Jekyll"
  - "archiving"
  - "Zenodo"
  - "Travis CI"
  - "GitHub action"
author: "Daniel Nüst"
---

The o2r project website's first entry [Introducing o2r]({% post_url 2016-01-19-introducing-o2r %}) was published [1132 days ago](https://www.timeanddate.com/date/durationresult.html?d1=19&m1=1&y1=2016&d2=24&m2=2&y2=2019).
Since then we've published short and long reports about events the o2r team participated in, advertised new scholarly publications we were lucky to have accepted in journals, and reported on results of workshops organised by o2r.
But there has also been some original content from time to time, such as the extensive articles on [Docker and R]({% post_url 2016-12-15-investigating-docker-and-R %}), which received several updates over the last years (some still pending), on the [integration of Stencila and Binder]({% post_url 2018-11-21-elife-sprint-integrating-stencila-and-binder %}), or on [writing reproducible articles for Copernicus Publications]({% post_url 2019-02-04-write-reproducible-manuscripts-for-copernicus-publications-journals %}).
These posts are a valuable output of the project, and contribute to the scholarly discussion.
Therefore, when it came to writing a report on the project's activities and outputs, it was time to consider the [preservation](https://en.wikipedia.org/wiki/Digital_preservation) of the project website and blog.
The website is built with [Jekyll](http://jekyllrb.com/) (with Markdown source files) and [hosted with GitHub pages](https://github.com/o2r-project/o2r-project.github.io), but GitHub may disappear and Jekyll might stop working at some point.

_So how can we archive the blog post and website in a sustainable way, without any manual interference?_

Today's blog post documents the steps to automatically deposit the sources, the HTML rendering, a PDF rendering, and the whole git repository in a new version of a [Zenodo deposit](https://doi.org/10.5281/zenodo.1485437) with each new blog post using [Zenodo's DOI versioning](help.zenodo.org#versioning).
The PDF was especially tricky but is very important, because the format is established for archival of content, while using the Zenodo API was pretty straightforward.
We hope the presented workflow might be useful for other websites and blogs in a scientific context.
It goes like this:

1. The [Makefile](https://en.wikipedia.org/wiki/Makefile) target `update_zenodo_deposit` starts the whole process with `make update_zenodo_deposit`. It triggers several other make targets, some of which require two processes to run at the same time:
1. Remove previously existing outputs ("clean").
1. Build the whole page with Jekyll and [serve](https://jekyllrb.com/docs/usage/) it using a local web server.
1. Create a PDF from the whole website from the local web server using [`wkhtmltopdf`](https://wkhtmltopdf.org/) and the special page [/all_content](/all_content), which renders _all_ blog entries in a suitable layout together with an automatically compiled list of author names and all website pages, unless they are excluded from the menu (e.g. manual redirection/shortened URLs) or excluded from "all pages" (e.g. the 404 page, blogroll, or publications list).
1. Create a ZIP archive with the sources, HTML rendering and PDF capture.
1. Run a Python script to upload the PDF and ZIP files to Zenodo using the [Zenodo API](http://developers.zenodo.org/), which includes several requests to retrieve the latest version metadata, check that there really is a new blog post, create a new deposit, remove the existing files in the deposit, upload the new files, and eventually publish the record.
1. Kill the still running web server.

For these steps to run automatically, the ~~[Travis CI](https://travis-ci.org/) configuration file, [`.travis.yml`](https://github.com/o2r-project/o2r-project.github.io/commit/5699871682178c500fe02fead163640cb480ea6f) (link to commit where Travis CI configuration was removed in favour of...)~~ the GitHub action configuration [`deposit.yml`](https://github.com/o2r-project/o2r-project.github.io/blob/master/.github/workflows/deposit.yml), installs the required software environment to conduct all above steps during each change to the main branch.
A secure environment variable for the repository is used to store a Zenodo API key, so the build system can manipulate the record.
The first version of this record, including its description, authors, tags, etc., was created manually.

[![Zenodo record screenshot](/public/images/2019-02_zenodo-record-screenshot.png){:width="300" .img.rightfloat}](https://doi.org/10.5281/zenodo.1485437)

_So what is possible now?_
As pointed out in the citation note at the bottom of pages and posts, the Digital Object Identifier ([DOI](https://en.wikipedia.org/wiki/Digital_object_identifier)) allows referencing the whole website or specific posts (via pages in the PDF) in scholarly publications.
Manual archival from a local computer is still possible by triggering the same make target.
As long as Zenodo exists, readers have access to all content published by the o2r research project on its website.

There are no specific next steps planned, but there's surely room for improvement as the current workflow is pretty complex.
The post publication date is the trigger for a new version, so changes in a page such as [About](/about) or in an existing post requires a manual triggering of the workflow (and commenting out the check for a new post) or wait for the next blog entry.
The created PDF [could be made compliant](https://github.com/o2r-project/o2r-project.github.io/issues/29) with [PDF/A](https://en.wikipedia.org/wiki/PDF/A).
The control flow could also be implemented completely in Python instead of using multiple files and languages; a Python module might even properly manage the system dependencies.
Though large parts of the process are not limited to pages generated with Jekyll (the capturing and uploading), it might be effectively wrapped in a standalone Jekyll [Jekyll plugin](https://jekyllrb.com/docs/plugins/), or a combination of a Zenodo plugin together with the (stale?) [`jekyll-pdf` plugin](https://github.com/abeMedia/jekyll-pdf)?
_Your feedback is very welcome!_
