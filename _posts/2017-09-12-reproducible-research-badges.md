---
layout: post
title: Reproducible Research Badges
categories:
  - badges
  - research
  - chrome extension
  - reproducible research
  - research badge
  - reproducibility
  - reproducible geosciences
author: 'Lukas Lohoff, Daniel Nüst'
---

*This blog post presents work based on the study project [Badges for computational geoscience containers](https://zivgitlab.uni-muenster.de/geocontainer-badges) at [ifgi](https://www.uni-muenster.de/Geoinformatics/). We thank the [project team](https://github.com/o2r-project/o2r-badger#contributors) for their valuable contributions!*

## Introduction

Today badges are widely used in open source software repositories. They have a high recognition value and consequently provide an easy and efficient way to convey up-to-date metadata. Version numbers, download counts, test coverage or container image size are just a few examples. The website [Shields.io](https://shields.io) provides many types of such badges. It also has an API to generate custom ones.

Now imagine similar badges, i.e. succinct, up-to-date information, not for software projects <!--more-->but for modern research publications. It answers questions such as: 

- When was a research paper published?
- Is the paper openly accessible?
- Was the paper published in a peer reviewed journal?
- What is the research's area of interest?
- Are the results reproducible?

These questions cover basic information for publications (date, open access, peer review) but also advanced concepts: the *research location* describes the location a study is focusing on. A publication with *reproducible results* contains a computation or analysis and the means to rerun it - ideally getting the same results again. 

We developed a back-end service providing badges for reproducible research papers.

## Overview of badges for research

We are however not the first nor the only ones to do this: [ScienceOpen](https://www.scienceopen.com/) is a search engine for scientific publications. It has badges for open access publications, content type, views, comments and the [Altmetric](https://www.altmetric.com/) score as displayed in Figure 1.

![scienceopen badges](/public/images/2017-09-12-badges/scienceOpen.png "Figure 1: ScienceOpen badges")
<p class="attributionInlineImage">Figure 1: <em>ScienceOpen</em> badges in a search result listing.</p>

These are helpful when using the ScienceOpen website, but they are not available for other websites. Additional issues are the inconsistent style and missing information relevant for reproducible geosciences, e.g. reproducibility status or the research location.

Badges are also used directly on publications, without the search portal "middleman". The published document, poster or presentation contains a badge along with the information needed to access the data or code.
The [Center for Open Science](https://cos.io/) [designed badges](https://osf.io/tvyxz/wiki/home/) for acknowledging open practices in scientific articles accompanied by guidelines for [incorporating them into journals' peer review workflows](https://osf.io/tvyxz/wiki/3.%20Incorporating%20Badges%20into%20Publication%20Workflow/) and [adding them to published documents](https://osf.io/tvyxz/wiki/4.%20Incorporating%20Badge%20Visualization%20into%20Publications/), including large colored and small black-and-white variants. The badges are for _Open Data_, _Open Materials_, and _Preregistration_ of studies (see Figure 2) and are adopted by over a dozen of journals to date (cf. [Adoptions and Endorsements](https://osf.io/tvyxz/wiki/5.%20Adoptions%20and%20Endorsements/)). 

![COS badges](/public/images/2017-09-12-badges/cos.png "Figure 2: COS badges"){:width="400"}
<p class="attributionInlineImage">Figure 2: <em>COS</em> badges.</p>

University of Washington’s [eScience Institute](http://escience.washington.edu/) created a peer-review process for open data and open materials badges [https://github.com/uwescience-open-badges/about](https://github.com/uwescience-open-badges/about) based on the COS badges. The service is meant for faculty members and students at the University of Washington, but external researchers can also apply. The initiative also has a list of relevant [publications on the topic](https://github.com/uwescience-open-badges/about#where-can-i-read-more-about-this).

A study by Kidwell et al. [[1](#kidwell)] demonstrates a positive effect by the introduction of open data badges in the journal *Psychological Science*: After the journal started awarding badges for open data, more articles stating open data availability actually published data (cf. [[2](#baker)]). They see badges as a simple yet effective way to promote data publishing. The argument is very well summarized in the tweet below:

<blockquote class="twitter-tweet" data-lang="de"><p lang="en" dir="ltr">Simple rewards are sufficient to see the change we want to occur <a href="https://twitter.com/hashtag/SSP2017?src=hash">#SSP2017</a> <a href="https://t.co/P1H4hpQeqN">pic.twitter.com/P1H4hpQeqN</a></p>&mdash; David Mellor (@EvoMellor) <a href="https://twitter.com/EvoMellor/status/870409694367666176">1. Juni 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Peng [[3](#peng1), [4](#peng2)] reports on the efforts the journal _Biostatistics_ is taking to promote reproducible research, including a set of _"kite marks"_, which can easily be seen as minimalistic yet effective badges. _**D**_ and _**C**_ if data respectively code is provided, and _**R**_ if results were successfully reproduced during the review process (implying D and C). Figure 3 shows the usage of **R** on an article's title page (cf. [[5](#lee)]).

![Biostatistics badges](/public/images/2017-09-12-badges/biostatistics-kitemark.png "Figure 3: Biostatistics kite marks"){:width="400"}
<p class="attributionInlineImage">Figure 3: <em>Biostatistics</em> kite mark <b>R</b> rendering in the PDF version of the paper.</p>

The Association for Computing Machinery ([ACM](https://www.acm.org/)) provides a common terminology and standards for artifact review processes for its conferences and journals, see their policies website section on [Artifact Review Badging](https://www.acm.org/publications/policies/artifact-review-badging). The have a system of three badges with several levels accompanied by specific criteria. They can be independently awarded:

- _Artifacts Evaluated_ means artifacts were made available to reviewers and awarded the level _Functional_ or _Reusable_
- _Artifacts Available_ means a deposition in a repository ensures permanent and open availability (no evaluation)
- _Results Validated_ means a third party successfully obtained the same results as the author at the levels _Results Replicated_ (using, in part, artifacts provided by the author) or _Results Reproduced_ (without author-supplied artifacts)

Figure 4 shows a rendering of the ACM badges.

![ACM badges](/public/images/2017-09-12-badges/acm.png "Figure 4: ACM badges"){:width="500"}
<p class="attributionInlineImage">Figure 4: <em>ACM</em> badges, from left to right: Artifacts Evaluated – Functional, Artifacts Evaluated – Reusable, Artifacts Available, Results Replicated, and Results Reproduced. (Copyright &copy; 2017, ACM, Inc)</p>

Although these examples are limited to a specific journal, publisher, or institution, they show the potential of badges. They also show the diversity, limitations, and challenges in describing and awarding these badges.

For this reason, our goal is to explore sophisticated and novel badge types (concerning an article's reproducibility, research location, etc.) and to find out how to provide them independently from a specific journal, conference, or website.

## An independent API for research badges

Advanced badges to answer the above questions are useful for literature research, because they open new ways of exploring research by allowing to quickly judge the relevance of a publication, and they can motivate efforts towards openness and reproducibility. Three questions remain: How can the required data for the badges be found, ideally automatically? How can the information be communicated? How can it be integrated across independent, even competitive, websites?

Some questions on the data, such as the publication date, the peer review status and the open access status can already be answered by online research library APIs, for example those provided by [Crossref](https://www.crossref.org/) or [DOAJ](https://doaj.org/).
The [o2r API](https://o2r.info/api/) can answer the remaining questions about reproducibility and location: Knowing if a publication is reproducible is a core part of the o2r project. Furthermore, the location on which a research paper focuses can be extracted from spatial files published with an Executable Research Compendium [[6](#nuest)]. The metadata extraction tool [o2r-meta](https://github.com/o2r-project/o2r-meta) provides the latter feature, while the [ERC specification](https://o2r.info/erc-spec) and [o2r-muncher](https://github.com/o2r-project/o2r-muncher) micro service enable the former.

_How can we integrate data from these different sources?_

[o2r-badger](https://github.com/o2r-project/o2r-badger) is a *Node.js* application based on the [Express](https://expressjs.com/) web application framework. It provides an API endpoint to serve badges for reproducible research integrating multiple online services into informative badges on scientific publications. Its [RESTful API](https://github.com/o2r-project/o2r-badger#api-documentation-version-02) has routes for five different badge types:

- _executable_: Information about executability and reproducibility of a publication
- _licence_: licensing information
- _spatial_: a publication's area of interest
- _releasetime_: publication date
- _peerreview_: if and by which process the publication was peer reviewed

The API can be queried with URLs following the pattern `/api/1.0/badge/:type/:doi`. `:type` is one of the aforementioned types, and `:doi` is a publication's [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier) (DOI).

The badger currently provides badges using two methods: internally created SVG-based badges, and redirects to [shields.io](https://shields.io/).
The redirects construct a simple shields.io URL.
The SVG-based badges are called *extended* badges and contain more detailed information: the extended *license* badge for example has three categories (*code*, *data* and *text*, see Figure 5), which are [aggregated](https://github.com/o2r-project/o2r-badger/blob/master/controllers/license/license.js#L312) to single values (open, partially open, mostly open, closed) for the shields.io badge (see Figure 6). 

![license badge](/public/images/2017-09-12-badges/license_extended.svg "Figure 4: An extended *licence* badge reporting open data, text and code")
<p class="attributionInlineImage">Figure 5: An extended licence badge reporting open data, text and code.</p>

Extended badges are meant for websites or print publications of a single publication, e.g. an article's title page. They can be resized and alternatively provided pre-rendered as a PNG image. In contrast, the standard shields.io badges are smaller, text based badges. They still communicate the most important piece of information:

![shields.io badge](https://img.shields.io/badge/licence-open-44cc11.svg)
<p class="attributionInlineImage">Figure 6: An shields.io based small badge, based on the URL <a href="https://img.shields.io/badge/licence-open-44cc11.svg" >https://img.shields.io/badge/licence-open-44cc11.svg</a>.</p>

They excel at applications where space is important, for example search engines listing many research articles. They are generated on the fly when a URL is requested (e.g. `https://img.shields.io/badge/licence-open-44cc11.svg`) which specifies the text (e.g. `licence` and `open`) and the color (`44cc11` is a [HTML color code](http://html-color-codes.info/) for green).

Let's look at another example of an *executable* badge and how it is created.
The badge below is requested from the badger demo instance on the o2r server by providing the DOI of the publication for the `:doi` element in the above routes:

[`https://o2r.uni-muenster.de/api/1.0/badge/executable/10.1126%2Fscience.1092666`](https://o2r.uni-muenster.de/api/1.0/badge/executable/10.1126%2Fscience.1092666)

This URL requests a badge for the reproducibility status of the paper “Global Air Quality and Pollution” from *[Science](http://science.sciencemag.org/)* magazine identified by the DOI [`10.1126/science.1092666`](https://doi.org/10.1126/science.1092666). When the request is sent, the following steps happen in o2r-badger:

1. The badger tries to find a reproducible research paper (called Executable Research Compendium ([ERC](https://o2r.info/erc-spec/spec/)) via the o2r API. Internally this searches the database for ERC connected to the given DOI.
2. If if finds an ERC, it looks for a matching *[job](https://o2r.info/api/job/)*, a report of a reproduction analysis.
3. Depending on the reproduction result (`success`, `running`, or `failure`) specified in the job, the badger generates a green, yellow or red badge. The badge also contains text indicating the reproducibility of the specified research publication.
4. The request is redirected to a [shields.io](https://shields.io/) URL link containing the color and textual information..

The returned image contains the requested information, which is in this case a successful reproduction:

URL: [https://img.shields.io/badge/executable-yes-44cc11.svg](https://img.shields.io/badge/executable-yes-44cc11.svg)

Badge: ![shields.io badge executable](https://img.shields.io/badge/executable-yes-44cc11.svg)

 If an extended badge is requested, the badger itself generates an SVG graphic instead.

Badges for reproducibility, peer review status and license are color coded to provide visual aids. They indicate for example (un)successful reproduction, a public peer review process, or different levels of open licenses.
These badges get their information from their respective external sources: the information for peer review badges is requested from the external service *DOAJ*, a community-based website for open access publications. The *Crossref* API provides the dates for the releasetime badges. The spatial badge also uses the o2r services. The badger service converts the spatial information provided as coordinates into textual information, i.e. place names, using the [Geonames API](http://www.geonames.org/export/web-services.html).

## Spread badges over the web

There is a great badge server, and databases providing manifold badge information, but how to get them displayed online? The sustainable way would be for research website operators to agree on a common badge system and design, and then incorporate these badges on their platforms. But we know it is unrealistic this ever happens.
So instead of waiting, or instead of engaging in a lengthy discourse with all stakeholders, we decided to create a [Chrome extension](https://developer.chrome.com/extensions) and augment common research websites. The [o2r-extender](https://github.com/o2r-project/o2r-extender) automatically inserts badges into search results or publication pages using client-side browser scripting. It is [available in the Chrome Web Store](https://chrome.google.com/webstore/detail/opening-reproducible-rese/fhhfncpkfohlhphlcgpkbpialfhkmbil) and ready to be tried out.

The extender currently supports the following research websites:

- Google Scholar [https://scholar.google.de/](https://scholar.google.de/)
- DOAJ.org [https://doaj.org/](https://doaj.org/)
- ScienceDirect.com [http://www.sciencedirect.com/](http://www.sciencedirect.com/)
- ScienceOpen.com [https://scienceopen.com/](https://scienceopen.com/)
- PLOS.org [https://www.plos.org/](https://www.plos.org/)
- Microsoft Academic [https://academic.microsoft.com/](https://academic.microsoft.com/)
- Mendeley [https://www.mendeley.com/](https://www.mendeley.com/)

For each article display on these websites, the extender requests a set of badges from the badger server. These are then inserted into the page’s HTML code after rendering the regular website as shown exemplary in the screenshot in Figure 7.

![google scholar badges](/public/images/2017-09-12-badges/google_scholar_badges.png "Figure 7: Badges integrated into Google Scholar search results")
<p class="attributionInlineImage">Figure 7: Badges integrated into <em>Google Scholar</em> search results (partial screenshot).</p>

When the badger does not find information for a certain DOI, it returns a grey “not available” - badge instead. This is shown in the screenshot above for the outermost license and peer review badges. 

The extender consists of a content script, similar to a [userscript](http://techsupportguides.com/what-is-a-userscript/), adjusted to each target website. The content scripts insert badges at suitable positions in the view. A set of common functions defined in the Chrome extension for generating HTML, getting metadata based on DOIs, and inserting badges are used for the specific insertions. A good part of the extender code is used to extract the respetive DOIs from the information included in the page, which is a lot trickier than interacting with an API. Take a look at the source code [on GitHub](https://github.com/o2r-project/o2r-extender/tree/master/extension) for details.

But the extender is not limited to inserting static information. The results of searches can also be filtered based on badge value and selected badge types can be turned on or off directly from the website with controls inserted into the pages' navigation menus (see left hand side of Figure 8).

![doaj filtering](/public/images/2017-09-12-badges/doaj_badges.png "Figure 8: Filtering search results on DOAJ")
<p class="attributionInlineImage">Figure 8: Filtering search results on <em>DOAJ</em>. Results not matching the filter or articles where the DOI could not be detected are greyed out.</p>

The extender is easily configurable: it can be enabled and disabled with a click on the icon in the browser toolbar. You can select the badge types to be displayed in the extension settings. Additionally it contains links to local info pages ("Help" and "About", see Figure 9).

![extender config](/public/images/2017-09-12-badges/extender_configuration.png "Figure 9: *o2r-extender* configuration")
<p class="attributionInlineImage">Figure 9: extender configuration.</p>

## Outlook: Action integrations

The *extender* also has a feature unrelated to badges. In the context of open science and reproducible research, the reproducibility service connects to other services in a larger context as described in the [o2r architecture](https://o2r.info/architecture/) (see section Business context).

Two core connections are loading research workspaces from cloud storage and connecting to suitable data repositories for actual storage of ERCs.
To facilitate these for users, the extender can also augment the user interfaces of the non-commercial cloud storage service [Sciebo](http://sciebo.de/) and the scientific data repository [Zenodo](https://zenodo.org/) with reproducibility service functionality.

When using *Sciebo*, a button is added to a file's or directory's context menu. It allows direct interaction with the o2r platform to upload a new reproducible research paper (ERC) from the current file or directory as shown in Figure 10.

![sciebo integration](/public/images/2017-09-12-badges/sciebo_integration.png "Figure 10: *Sciebo* upload integration")
<p class="attributionInlineImage">Figure 10: <em>Sciebo</em> upload integration.</p>

When you are viewing an *Executable Research Compendium* on *Zenodo*, a small badge links directly to the corresponding inspection view in the o2r platform (see Figure 11):

![zenodo integration](/public/images/2017-09-12-badges/zenodo_integration.png "Figure 11: Zenodo inspection integration")
<p class="attributionInlineImage">Figure 11: Link to inspection view and tag "ERC" on <em>Zenodo</em>.</p>

## Discussion

The study project [Badges for computational geoscience containers](https://zivgitlab.uni-muenster.de/geocontainer-badges) initially implemented eight microservices responsible for six different badges types, badge scaling and testing. A microservice architecture using Docker containers was not chosen because of the need for immense scaling capabilities, but for another reason: developing independent microservices makes work organization much easier. This is especially true for a study project where students prefer different programming languages and have different skill sets.

However, for o2r the microservices were integrated into a single microservice for easier maintainability. This required refactoring, rewriting and bug fixing.
Now, when a badge is requested, a [promise chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) is executed (see [source code example](https://github.com/o2r-project/o2r-badger/blob/master/controllers/executability/executability.js#L83)). The chain reuses functions across all badges where possible, which were refactored from the study project code into small chunks to avoid [callback hell](http://callbackhell.com/).

A critical feature of extender is the detection of the DOI from the website's markup. For some websites, such as *DOAJ.org* or *ScienceOpen.com*, this is not hard because they provide the DOI directly for each entry.
When the DOI is not directly provided, the extender tries to retrieve the DOI from a request to *CrossRef.org* using the paper title (see [source code for the DOI detection](https://github.com/o2r-project/o2r-extender/blob/master/extension/BaseImplementation.js#L447)). This is not always successful or may find incorrect results.

The Chrome extension supports nine different websites. If there are changes to one of these, the extender has to be updated as well. For example, [Sciebo](http://sciebo.de/) (based on [ownCloud](https://owncloud.org/)) recently changed their URLs to include a “fileid” parameter which resulted in an error when parsing the current folder path.

As discussed above, in an ideal world the Chrome extension would not be necessary. While there are a few tricky parts with a workaround like this, it nevertheless allows o2r as a research project to easily demonstrate ideas and prototypes stretching beyond the project's own code to even third party websites.
Moreover, the combination of extender client and badger service is suitable for embedding a common science badge across multiple online platforms. It demonstrates a technical solution how the scientific community can create and maintain a cross-publisher, cross-provider solution for research badges. What it clearly lacks is a well-designed and transparent workflow for awarding and scrutinizing badges.

## Future Work

One of the biggest source of issues for *badger* currently is the dependence on external services such as *Crossref* and *DOAJ*. While this cannot be directly resolved, it can be mitigated by requesting multiple alternative back-end services, which can provide the same information (e.g. *DOAJ* for example also offers licence information at least for publications), or even by caching.
Furthermore, the newness of the o2r platform itself is another issue: *licence*, *executable*, and *spatial* badges are dependent on an existing ERC, which must be linked via DOI to a publication. If a research paper has not been made available as an ERC then a users will get a lot of “n/a” badges.

The *extender* is only available for Google Chrome and Chromium. But since Firefox is switching to [WebExtensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions) and moving away from their old “add-ons” completely with [Firefox 57](https://developer.mozilla.org/en-US/Add-ons/Overlay_Extensions/Firefox_addons_developer_guide), a port from a Chrome Extension to the open *WebExtensions* makes the extender available for more users. The port should be possible with a few changes due to only minor differences between the two types of extensions.

Other ideas for further development and next steps include:

- Interactive badges can provide additional information when hovering over them or when the badges are clicked, most importantly why and by who the badge was assigned.
- Provide the information behind the badges via an API.
- Create a common design for extended badges.
- Conduct a user study on extended and basic badges within a discovery scenario.
- Evaluating usage of badges in print applications and for visually impaired people (cf. COS badges)

For more see the GitHub issues pages of [o2r-badger](https://github.com/o2r-project/o2r-badger/issues) and [o2r-extender](https://github.com/o2r-project/o2r-extender/issues). Any feedback and ideas are appreciated, either on the GitHub repositories or in [this discussion thread](https://groups.google.com/d/topic/reproducible-research/AP0k_xi69AA/discussion) in the Google Group [_Scientists for Reproducible Research_](https://groups.google.com/forum/#!forum/reproducible-research). We thank the group members for pointing to some of the resources referenced in this post.

## References

<a name="kidwell"></a>[1] Kidwell, Mallory C., et al. 2016. Badges to Acknowledge Open Practices: A Simple, Low-Cost, Effective Method for Increasing Transparency. <em>PLOS Biology</em> 14(5):e1002456. doi:<a href="https://doi.org/10.1371/journal.pbio.1002456">https://doi.org/10.1371/journal.pbio.1002456</a>.

<a name="baker"></a>[2] Baker, Monya, 2016. Digital badges motivate scientists to share data. <em>Nature News</em>. doi:<a href="https://doi.org/10.1038/nature.2016.19907">10.1038/nature.2016.19907</a>.
<!-- https://www.nature.com/news/digital-badges-motivate-scientists-to-share-data-1.19907 -->

<a name="peng1"></a>[3] Peng, Roger D. 2009. Reproducible research and Biostatistics. Biostatistics, Volume 10, Issue 3, Pages 405–408. doi:<a href="https://doi.org/10.1093/biostatistics/kxp014">10.1093/biostatistics/kxp014</a>.

<a name="peng2"></a>[4] Peng, Roger D. 2011. Reproducible Research in Computational Science. Science 334 (6060): 1226–27. doi:<a href="https://doi.org/10.1126/science.1213847">10.1126/science.1213847</a>.

<a name="lee"></a>[5] Lee, Duncan, Ferguson, Claire, and Mitchell, Richard. 2009. Air pollution and health in Scotland: a multicity study. Biostatistics, Volume 10, Issue 3, Pages 409–423, doi:<a href="https://doi.org/10.1093/biostatistics/kxp010">10.1093/biostatistics/kxp010</a>.

<a name="nuest"></a>[6] Nüst, D., Konkol, M., Pebesma, E., Kray, C., Schutzeichel, M., Przibytzin, H., and Lorenz, J. Opening the Publication Process with Executable Research Compendia. D-Lib Magazine. 2017. doi:<a href="https://doi.org/10.1045/january2017-nuest">10.1045/january2017-nuest</a>.
