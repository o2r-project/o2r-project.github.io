---
layout: post
title: Reference Implementation - Try it out!
categories:
  - research
  - reproducible research
  - reference implementation
  - code
  - GitHub
  - Zenodo
  - Docker
author: 'Daniel Nüst'
---

Our project is going into its final phase. We are [working on](https://github.com/o2r-project/erc-spec/pull/48) integrating our latest experiences and discussions into the [ERC specification](http://o2r.info/erc-spec) and constantly add new features to the [implementation of the reproducibility service](https://github.com/o2r-project).

We also try to keep our [demo server](http://o2r.info/results/#implementation--demo) up to date.
_But what good is a reproducibility platform, when you can only try it online?_

Inspired by the just passed [Open Access Week](http://www.openaccessweek.org/) ([#oaweek](https://twitter.com/hashtag/OAWeek?src=hash)), we've started [a new repository `reference-implementation`](https://github.com/o2r-project/reference-implementation/issues) to expose our developments, which have been open source from the start, to the interested public.

![o2r screenshot: Ubuntu](/public/images/2017-10-31-refimpl/o2r-refimpl-ubuntu.jpg "Screenshot: o2r reference implementation on Ubuntu"){:width="600"}
<p class="attributionInlineImage">Screenshot: o2r reference implementation on <em>Ubuntu</em>.</p>
![o2r screenshot: OS X](/public/images/2017-10-31-refimpl/o2r-refimpl-macos-x.jpg "Screenshot: o2r reference implementation on Mac OS X"){:width="600"}
<p class="attributionInlineImage">Screenshot: o2r reference implementation on <em>OS X</em>.</p>

It comprises documentation for run o2r software on a completely new machine:

- [Run o2r locally with pre-build Docker images](https://github.com/o2r-project/reference-implementation#download-images-and-run) (the regular approach, let's you easily update to later versions)
- [Download all source code, build Docker images, and then run o2r locally](https://github.com/o2r-project/reference-implementation#build-images-from-source-and-run) (the investigative approach)
- Upload a [demo workspace or ERC](https://github.com/o2r-project/erc-examples)

The only efforts besides a few commands on your computer is [registering a client application with ORCID](https://support.orcid.org/knowledgebase/articles/343182-register-a-public-api-client-application) to be able to log in, because there is no other way to authenticate within the o2r platform and microservices.
You may also [get an access token from Zenodo](https://zenodo.org/login/?next=%2Faccount%2Fsettings%2Fapplications%2Ftokens%2Fnew%2F) to "ship" your completed ERC.
Eventually this repository will be the basis for a citable package of our software.

We look forward to [your feedback](https://github.com/o2r-project/reference-implementation/issues)!

## `tl;dr`

1. Install [Docker](https://www.docker.com/get-docker), [docker-compose](https://docs.docker.com/compose/), and [make](https://en.wikipedia.org/wiki/Make_(software))
1. Register your own [client application at ORCID](https://github.com/o2r-project/reference-implementation#orcid))
1. Download the o2r reference implementation repository and run it with with <br />
  - `git clone https://github.com/o2r-project/reference-implementation`
  - `O2R_ORCID_ID=<your orcid id> O2R_ORCID_SECRET=<your orcid secret> O2R_ORCID_CALLBACK=http://localhost/api/v1/auth/login make run_hub`

![o2r screenshot: Windows 10](/public/images/2017-10-31-refimpl/o2r-refimpl-windows10.jpg "Screenshot: o2r reference implementation on Windows 10"){:width="600"}
<p class="attributionInlineImage">Screenshot: o2r reference implementation on <em>Windows 10</em>.</p>

![o2r screenshot: Windows 10 with Docker Toolbox](/public/images/2017-10-31-refimpl/o2r-refimpl-windows10-toolbox.jpg "Screenshot: o2r reference implementation on Windows 10 with Docker Toolbox"){:width="600"}
<p class="attributionInlineImage">Screenshot: o2r reference implementation on <em>Windows 10</em> (Docker Toolbox), contributed by Antonia - Thanks!</p>
