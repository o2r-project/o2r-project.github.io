---
layout: post
title: Reproducible Research at EGU GA - A short course recap
categories:
  - workshop
  - EGU
  - recap
  - shourt course
  - general assembly
author: 'Daniel Nüst, Vicky Steeves, Rémi Rampin'
---

At last week’s [EGU general assembly](http://egu2017.eu/) members of the [o2r](https://o2r.info) and [ReproZip](https://reprozip.org/) projects organized the short course [_“Reproducible computational research in the publication cycle”_](http://meetingorganizer.copernicus.org/EGU2017/session/25726). This post is a recap of the course by [Daniel Nüst](http://danielnuest.de/), [Vicky Steeves](https://vickysteeves.com/), and [Rémi Rampin](https://remirampin.com/).

![short course room photo](/public/images/2017-05_egu-01.jpg "Ready to start - the short course room filling up"){:width="300" .img.rightfloat}

All **materials for the course are published in an Open Science Framework repository at [https://osf.io/umy6g/](https://osf.io/umy6g/)** and you can learn about the motivation for the course in the [course page at EGU](http://meetingorganizer.copernicus.org/EGU2017/session/25726).

The short was divided into two parts:<!--more--> a practical introduction to selected tools supporting computational reproducibility, and talks by stakeholders in the scientific publication process followed by a lively panel discussion.

**In the first part**, Daniel and Vicky began with sharing some literature on reproducible research (RR) with the roughly 30 participants. After all, the participants should take home something useful, so a reading list seems reasonable for RR newcomers but also for researchers writing about the reproducibility aspects in upcoming papers.

Then Daniel fired up a console and took a deep dive into **using containers to encapsulate environments for reproducible computational research**. He started with a very quick introduction to Docker and then demonstrated some containers useful to researchers, i.e. Jupyter Notebook and RStudio.

The material presented by Daniel is a [starting point for an Author Carpentry lesson](https://nuest.github.io/docker-reproducible-research/), which is currently [developed on GitHub](https://github.com/nuest/docker-reproducible-research), so he highly appreciates any feedback, especially by shourt course attendees. We were surprised to learn a good portion of the participants had already some experience with Docker. But even better was realizing a few actually hacked along as Daniel raced through command-line interface examples! This "raw" approach to packaging research in containers was contrasted in the second section.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">.<a href="https://twitter.com/nordholmen">@nordholmen</a> forked author carpentry to make a lesson for us today! About to look at rstudio &amp; jupyter notebooks w/ Docker!  <a href="https://twitter.com/hashtag/egu2017?src=hash">#egu2017</a> <a href="https://t.co/ekgYuJPkS6">pic.twitter.com/ekgYuJPkS6</a></p>&mdash; Vicky Steeves (@VickySteeves) <a href="https://twitter.com/VickySteeves/status/856475174165721088">April 24, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Under the title **"ReproZip for geospatial analyses"**, Vicky and Rémi showcased [ReproZip](https://reprozip.org), a tool for automatically tracing and packaging scientific analyses for easily achieved computational reproducibility. The resulting file is a ReproZip package (`.rpz`), which can be easily shared due to it’s small size, and contains everything necessary to reproduce research (input files, environmental information etc.) across different operating systems. They demonstrated their various unpackers and showed how these `.rpz` files can be used for reproducibility and archiving. They also demoed they brand new user interface for the first time in Europe.

The materials presented by Vicky and Rémi are also available on both the Open Science Framework [here](https://osf.io/umy6g/) and on the [ReproZip examples website](https://examples.reprozip.org).

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/edzerpebesma">@edzerpebesma</a> <a href="https://twitter.com/benmarwick">@benmarwick</a> <a href="https://twitter.com/o2r_project">@o2r_project</a> And <a href="https://twitter.com/VickySteeves">@VickySteeves</a>  and  <a href="https://twitter.com/remram44">@remram44</a> showing <a href="https://twitter.com/hashtag/reprozip?src=hash">#reprozip</a> <a href="https://t.co/4hxpEsmqPN">pic.twitter.com/4hxpEsmqPN</a></p>&mdash; Daniel Nüst (@nordholmen) <a href="https://twitter.com/nordholmen/status/856488328190930944">April 24, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The practical demonstrations paved the way for the **second part** of the short course, which was more abstract yet proofed to excellently demonstrate the breadth of reproducible research. Selected speakers provided their perspectives on the topic of reproducing scientific papers in the broader context of the scientific publication cycle. In short talks they wore a specific role of the scholarly publication process and shared their experience as as researcher, infrastructure provider, publisher, reviewer, librarian, or editor. The speakers:

- [Edzer Pebesma](https://orcid.org/0000-0001-8049-7069) talked about his experiences as journal editor for [JStatSoft](http://jstatsoft.org/) as well as [Computers & Geosciences](http://www.journals.elsevier.com/computers-and-geosciences/), and his original motivation to enter the area of reproducible research with [his prize-winning “one-click reproduce” concept](http://pebesma.staff.ifgi.de/epic.pdf) and initiator of [o2r](https://o2r.info): annoyance by not being able to share the full integrated material of his works easily.
- [Tobias Weigel](https://www.dkrz.de/about/Organisation/mitarbeiter/TobiasWeigel) from the [german national climate computing center](https://www.dkrz.de/dkrz-en?set_language=en&cl=en) introduced the challenges and limitations for a supercomputer facility which provides crucial resources for reproducibility.
- [David Ham](https://orcid.org/0000-0001-9545-9110) shared the priorities of the [journal Geoscientific Model Development (GMD)](http://www.geoscientific-model-development.net/) where he is editor, when it comes to reproducibility and the issues they face. Proper provenance and citations are examples for the former, the ephemerality of code and data for the latter.
- [Xenia van Edig](https://orcid.org/0000-0003-2510-0529) lead us through the stages of Open Access that [Copernicus](http://publications.copernicus.org/) went and is going through as a publisher: from public data (1.0) via interactive articles and public peer review (2.0) to the future of open science and executable papers (3.0)
- [Vicky Steeves](http://vickysteeves.com/) advertised the expertise of librarians worldwide in supporting research in all aspects, including reproducibility, writing grants, or data management plans, but also pointed out the necessity to support scientists with proper tools and teach the required skills.
- [Daniel Nüst](http://danielnuest.de/) (research software engineer perspective)

![short course discussion panel](/public/images/2017-05_egu-01.jpg "panel discussion photo"){:width="300" .img.rightfloat}

All speakers touched on the topic of _scientific culture_, which was seen in a process of changing towards more openness, but with still quite some way to go. The cultural aspects and larger scale challenges were a recurring topic in the panel discussion after the short talks. These aspects included resistance to share supplemental material, so that journals cannot make sharing everything mandatory, for example because of unwillingness (fear of stealing) or because authors might not be allowed to do so. A member of the audience could share that in their experience as a publisher, requiring data and software publication did not result in a decrease in submissions when accompanied by transparent and helpful author guidelines. Such guidelines for both data and code are lacking for many journals but are a means to improve the overall situation - and make the lives of editors simpler.
When the progress of the last years on Open _Data_ was pointed out as largely a top down political endeavour, the contrast to _Open Source_ as a bottom-up grassroots initiative became clear. Nevertheless, the hope was phrased that with the success of Open Data, things might go smoother with Open Source in science.

A further topic the discussion covered for some time was _creditation_, and the need to update the ways researchers get _and give_ credit as part of grant-based funding and publishing scholarly articles. Though it was pointed out that RR is also about “doing the right thing”. Credit and culture were seen as closely linked topics, which can only be tackled by improving the education of scientists, both as authors and reviewers(!), and spreading the word about the importance of reproducibility for all of science, not least in the light of the marches for sciences taking place just a few days before the short course.

While one could say we were mostly preaching to the choir, it was great to see an interest in the topic of reproducible research amongst EGU attendees. **This workshop being the first of its kind at the EGU general assembly hopefully was a step towards even higher visibility and interest for RR as a crucial topic in today’s research.**

We thank the short course attendees and invited speakers for turning the first afternoon of EGU 2017 into an instructive and diverting few hours. _Will there be a reproducible research short course next year at EGU?_ We don’t know yet, but please do get in touch if you would like to support the planning. It could be worth providing a longer course targeted as [early career scientists](http://www.egu.eu/ecs/), giving the [next generation](https://deevybee.blogspot.de/2017/05/reproducible-practices-are-future-for.html) the tools to work reproducibly.
