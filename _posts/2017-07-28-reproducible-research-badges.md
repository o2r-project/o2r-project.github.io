---
layout: post
title: Reproducible Research Badges
categories:
  - badges
  - research
  - chrome extension
author: 'Lukas Lohoff, Daniel Nüst'
---

*This blog post presents work based on the study project [Badges for computational geoscience containers](https://zivgitlab.uni-muenster.de/geocontainer-badges) at [ifgi](https://www.uni-muenster.de/Geoinformatics/). We thank the [project team](https://github.com/o2r-project/o2r-badger#contributors) for their great contributions!*

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

We are however not the first nor the only ones to do this: [ScienceOpen](https://www.scienceopen.com/) is a search engine for scientific publications. It has badges for open access publications, content type, views, comments and the [Altmetric](https://www.altmetric.com/) score:

![scienceopen badges](/public/images/2017-07-28-badges/scienceOpen.png "Figure 1: ScienceOpen badges")
<p class="attributionInlineImage">Figure 1: <em>ScienceOpen</em> badges.</p>

These are helpful when using the *ScienceOpen* website, but they are not available for other websites. Additional issues are the inconsistent style and missing information relevant for reproducible geosciences, e.g. reproducibility status or the research location.

Badges are also used directly on publications, without the search portal "middleman". The published document, poster or presentation contains a badge along with the information needed to access the data or code.
The [Center for Open Science](https://cos.io/) [designed badges](https://osf.io/tvyxz/wiki/home/) for acknowledging open practices in scientific articles accompanied by guidelines for [incorporating them into journals' peer review workflows](https://osf.io/tvyxz/wiki/3.%20Incorporating%20Badges%20into%20Publication%20Workflow/) and [adding them to published documents](https://osf.io/tvyxz/wiki/4.%20Incorporating%20Badge%20Visualization%20into%20Publications/), including large colored and small black-and-white variants. The badges are for _Open Data_, _Open Materials_, and _Preregistration_ of studies (see Figure 2) and are adopted by over a dozen of journals to date (cf. [3](https://osf.io/tvyxz/wiki/5.%20Adoptions%20and%20Endorsements/)). 

![COS badges](/public/images/2017-07-28-badges/cos.png "Figure 2: COS badges"){:width="400"}
<p class="attributionInlineImage">Figure 2: <em>COS</em> badges.</p>

University of Washington’s [eScience Institute](http://escience.washington.edu/) created a peer-review process for open data and open materials badges [https://github.com/uwescience-open-badges/about](https://github.com/uwescience-open-badges/about) based on the COS badges. The service is meant for faculty members and students at the University of Washington, but external researchers can also apply. The initiative also has a list of relevant [publications on the topic](https://github.com/uwescience-open-badges/about#where-can-i-read-more-about-this).

A study by Mallory C. Kidwell et al. [[1](#kidwell)] demonstrates a positive effect by the introduction of open data badges in the journal *Psychological Science*: After the journal started awarding badges for open data, more articles stating open data availability actually published data (cf. [[2](#baker)]). They see badges as a simple yet effective way to promote data publishing.

Peng [[4](#peng1), [5](#peng2)] reports on the efforts the journal _Biostatistics_ is taking to promote reproducible research, including a set of _"kite marks"_, which can easily be seen as minimalistic badges. _**D**_ and _**C**_ if data respectively code is provided, and _**R**_ if results were successfully reproduced during the review process (implying D and C). Figure 3 shows the usage of _R_ on an article's title page (cf. [[6](#lee)]).

![Biostatistics badges](/public/images/2017-07-28-badges/biostatistics-kitemark.png "Figure 3: Biostatistics kite marks"){:width="400"}
<p class="attributionInlineImage">Figure 3: <em>Biostatistis</em> kite mark <em>R</em> rendering in the PDF version of the paper.</p>

The Association for Computing Machinery ([ACM](https://www.acm.org/)) provides a common terminology and standards for artifact review processes for its conferences and journals, see their policies website section on [Artifact Review Badging](https://www.acm.org/publications/policies/artifact-review-badging). The have a system of three badges with several levels accompanied by specific criteria. They can be independently awarded:

- _Artifacts Evaluated_ means artifacts were made available to reviewers and awarded the level _Functional_ or _Reusable_
- _Artifacts Available_ means a deposition in a repository ensures permanent and open availability (no evaluation)
- _Results Validated_ means a third party successfully obtained the same results as the author at the levels _Results Replicated_ (using, in part, artifacts provided by the author) or _Results Reproduced_ (without author-supplied artifacts)

Figure 4 shows a rendering of the ACM badges.

![ACM badges](/public/images/2017-07-28-badges/acm.png "Figure 4: ACM badges"){:width="500"}
<p class="attributionInlineImage">Figure 4: <em>ACM</em> badges, from left to right: Artifacts Evaluated – Functional, Artifacts Evaluated – Reusable, Artifacts Available, Results Replicated, and Results Reproduced. (Copyright &copy; 2017, ACM, Inc)</p>


Although these examples are limited to a specific journal, publisher, or institution, they show the potential impact of badges. They also show the diversity, limitations, and challenges in describing and awarding these badges.

For this reason, our goal is to explore sophisticated and novel badge types (reproducibility, research location, etc.) and to find out how to provide them independently from a specific journal, conference, or website.

## An independent API for research badges

Advanced badges to answer the above questions are useful when doing literature research. They open new ways of exploring research. Now the question remains how the required information for the badges can be found out automatically. 

Questions, such as the publication date, the peer review status and the open access status can already be answered by online research library APIs, i.e. [Crossref](https://www.crossref.org/) or [DOAJ](https://doaj.org/).

The [o2r API](http://o2r.info/o2r-web-api/) can (or will be able to) answer the remaining questions about reproducibility and location: Knowing if a publication is reproducible is a core part of this project. Furthermore, the location on which a research paper focuses is extracted from spatial files published with the publication. For this task, [o2r-meta](https://github.com/o2r-project/o2r-meta), a metadata extraction tool, was developed.

How can we integrate the information from these different sources?

[o2r-badger](https://github.com/o2r-project/o2r-badger) is a *Node.js* application. It provides an API endpoint based on the [Express](https://expressjs.com/) web application framework. The API serves badges for reproducible research with information from multiple online services. It has routes for five different badge types:

- `/badge/executable/:id`
- `/badge/licence/:id`
- `/badge/spatial/:id`
- `/badge/peerreview/:id`
- `/badge/releasetime/:id`

The badger currently provides two kinds of badges: internally created SVG-based badges, and redirects to [shields.io](https://shields.io/). The SVG-based badges are called *extended* badges and often contain more precise information: the extended *license* badge for example has three categories (*code*, *data* and *text*) of openness. This is to converted to a single value in the standard *shields.io* badge. 

![license badge](/public/images/2017-07-28-badges/license_extended.svg "Figure 3: An extended *licence* badge reporting open data, text and code")
<p class="attributionInlineImage">Figure 3: An extended licence badge reporting open data, text and code</p>

Extended badges are meant for posters or websites that focus on a single publication. They can be resized and provided as a PNG image using the API parameters. See the badger [API documentation](https://github.com/o2r-project/o2r-badger#api-documentation-version-02) for more info. In contrast, the standard shields.io badges are smaller, text based badges. They still communicate the most important piece of information:

![shields.io badge](https://img.shields.io/badge/licence-open-44cc11.svg)
 
They excel at applications where space is important, for example search engines that list many research articles. [Shields.io](https://shields.io/) generates these SVG images on the fly when a URL is requested (e.g. `https://img.shields.io/badge/licence-open-44cc11.svg`) which specifies the text (`licence` and `open`) and the color (`44cc11` is a [HTML color code](http://html-color-codes.info/) for green).

How can the badges be utilized? Firstly, they are ready to be integrated into other projects or websites. Here is an example of an *executable* badge: The badge is requested from the badger instance on the o2r server by providing the DOI of the publication for the `:id` element in the above routes, for example

[`https://o2r.uni-muenster.de/api/1.0/badge/executable/10.1126%2Fscience.1092666`](https://o2r.uni-muenster.de/api/1.0/badge/executable/10.1126%2Fscience.1092666)

This URL requests a badge for the reproducibility status of the paper “Global Air Quality and Pollution” from *[Science](http://science.sciencemag.org/)* magazine identified by the DOI [`10.1126/science.1092666`](https://doi.org/10.1126/science.1092666). When the request is sent, the following steps happen:

1. The badger tries to find a reproducible research paper (called Executable Research Compendium ([ERC](http://o2r.info/erc-spec/spec/)) inside the *o2r platform*. This is done by searching the database for the given DOI.
2. If if finds an ERC, it looks for a matching *[job](http://o2r.info/o2r-web-api/job/)*, a report of a reproduction analysis.
3. Depending on the reproduction result (`success`, `running`, or `failure`) specified in the job, the badger generates a green, yellow or red badge. The badge also contains text indicating the reproducibility of the specified research publication.
4. The request is redirected to a [shields.io](https://shields.io/) URL link containing the color and textual information. If an extended badge is requested, the badger generates and sends a SVG graphic instead.

The returned image contains the requested information, which is in this case a successful reproduction:

URL: [https://img.shields.io/badge/executable-yes-44cc11.svg](https://img.shields.io/badge/executable-yes-44cc11.svg)

Badge: ![shields.io badge executable](https://img.shields.io/badge/executable-yes-44cc11.svg)

Badges for reproducibility, peer review status and license are color coded to provide additional visual aids. This indicates for example (un)successful reproduction.

Other badges get their information from external sources: the information for peer review badges is requested from the external service *DOAJ*, a community-based website for open access publications. The *Crossref* API provides the dates for the releasetime badges. The spatial badge also uses the o2r services, but it additionally converts the spatial information from coordinates into textual information, i.e. place names. For the conversion, it is using the [Geonames API](http://www.geonames.org/export/web-services.html). 

## Spread badges over the web

There is a great badge server, and databases providing manifold badge information, but how to get them displayed online? The sustainable way would be for research website operators to agree on a common badge system and design, and then incorporate these badges on their platforms. But we know that is never ever going to happen. So instead of waiting we created a [Chrome extension](https://developer.chrome.com/extensions) for common research websites. The [o2r-extender](https://github.com/o2r-project/o2r-extender) automatically inserts badges into search results or publication pages using client-side browser scripting. Its available in the Chrome Web Store (*[here](https://chrome.google.com/webstore/detail/opening-reproducible-rese/fhhfncpkfohlhphlcgpkbpialfhkmbil)*) and ready to be tried out.

The extender currently supports the following websites:

- Google Scholar [https://scholar.google.de/](https://scholar.google.de/)
- DOAJ.org [https://doaj.org/](https://doaj.org/)
- ScienceDirect.com [http://www.sciencedirect.com/](http://www.sciencedirect.com/)
- ScienceOpen.com [https://scienceopen.com/](https://scienceopen.com/)
- PLOS.org [https://www.plos.org/](https://www.plos.org/)
- Microsoft Academic [https://academic.microsoft.com/](https://academic.microsoft.com/)
- Mendeley [https://www.mendeley.com/](https://www.mendeley.com/)

For each listed article contained in these research websites, the extender requests a set of badges from the *o2r-badger*. These are then inserted into the page’s HTML code after rendering the regular website:

![google scholar badges](/public/images/2017-07-28-badges/google_scholar_badges.png "Figure 3: Badges integrated into Google Scholar search results")
<p class="attributionInlineImage">Figure 3: Badges integrated into <em>Google Scholar</em> search results</p>

When the badger does not find information for a certain DOI, it returns a grey “not available” - badge instead. This is shown in the screenshot above for the outermost license and peer review badges. 

The *extender* consists of a content script, similar to a [userscript](http://techsupportguides.com/what-is-a-userscript/), for each research website. The content scripts insert a set of badges (Figure 3) for each article in the respective website. They all use a set of base functions defined in the Chrome extension for generating HTML, getting DOIs and inserting badges. The source code is available on [GitHub](https://github.com/o2r-project/o2r-extender/tree/master/extension).

The listed results on each website can also be filtered based on badge values. Additionally selected badge types can be turned on or off directly from the website with controls. These filters and controls are also inserted into the page (see left hand side of Figure 4). Results not matching the filter or articles where the DOI could not be detected are greyed out.

![doaj filtering](/public/images/2017-07-28-badges/doaj_badges.png "Figure 4: Filtering search results on DOAJ")
<p class="attributionInlineImage">Figure 4: Filtering search results on <em>DOAJ</em></p>

### Configuration

The extender is easily configurable: it can be enabled and disabled with a click on the icon in the browser toolbar. You can select the badge types to be displayed in the extension settings. Additionally it contains links to local info pages (“Help” and “About”), explaining the *extender* and the different badge types:

![extender config](/public/images/2017-07-28-badges/extender_configuration.png "Figure 5: *o2r-extender* configuration")
<p class="attributionInlineImage">Figure 5: <em>o2r-extender</em> configuration</p>

## Outlook: Action integrations

The *extender* also has a feature unrelated to badges. In the context of open science and reproducible research, we place the reproducibility service in a larger context as described in the [o2r architecture](http://o2r.info/architecture/) (see section Business context). Two core aspects are loading research workspaces from cloud storage and connecting to suitable data repositories for actual storage of ERCs.

To facilitate this integration for users, the extender can also augment the user interfaces of the cloud collaboration platform [Sciebo](http://sciebo.de/) and the scientific data repository [Zenodo](https://zenodo.org/) to integrate our reproducibility service.

When using *Sciebo*, a button is added  to a file’s or directory’s context menu. It allows direct interaction with the o2r platform to upload a new reproducible research paper (called ERC) from the current file or directory.

![sciebo integration](/public/images/2017-07-28-badges/sciebo_integration.png "Figure 6: *Sciebo* upload integration")
<p class="attributionInlineImage">Figure 6: <em>Sciebo</em> upload integration</p>

When you are viewing an *Executable Research Compendium* on *Zenodo*, a small badge redirects to the inspection view in the *o2r platform*:

![zenodo integration](/public/images/2017-07-28-badges/zenodo_integration.png "Figure 7: Zenodo inspection integration")
<p class="attributionInlineImage">Figure 7: <em>Zenodo</em> inspection integration</p>

## Challenges

The study project [Badges for computational geoscience containers](https://zivgitlab.uni-muenster.de/geocontainer-badges) initially implemented eight microservices responsible for six different badges types, badge scaling and testing. A microservice architecture using Docker containers was not chosen because of the need for immense scaling capabilities, but for another reason: developing independent microservices makes work organization much easier. This is especially true for a study project where students prefer different programming languages and have different skillsets.

However, for the *o2r project*, the eight microservices needed to become a single microservice. This required refactoring, rewriting and bug fixing. Now, when a badge is requested, a [promise chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) is called (source code example [here](https://github.com/o2r-project/o2r-badger/blob/master/controllers/executability/executability.js#L83)) depending on the badge type. It consists of a number of functions of which some are used by all badges. The functions each contain code written in the study project separated into small chunks to avoid a [callback hell](http://callbackhell.com/).

In the *extender*, a critical feature is the detection of the DOI just from a research paper title. For some websites such as *DOAJ.org* or *ScienceOpen.com* this is not necessary, as they provide the DOI directly for each entry. But when the DOI is not directly provided, the *extender* tries to get the DOI from a request to *CrossRef.org*. This is not always successful or may find incorrect results depending on the paper title ([source code](https://github.com/o2r-project/o2r-extender/blob/master/extension/BaseImplementation.js#L447) for the DOI detection).
As discussed above, in an ideal world the *o2r-extender* Chrome extension would not be necessary. There are a few tricky parts with a workaround like this: The extension supports nine different websites. If there are changes to one of these, the *extender* has to be updated as well. For example, [Sciebo](http://sciebo.de/), an [OwnCloud](https://owncloud.org/) implementation, recently changed their URLs to include a “fileid” parameter which resulted in an error when parsing the current folder path.

## Future Work

There is still potential for future improvements: one of the biggest current issues is the dependence on external services such as *Crossref* and *DOAJ*. While this issue cannot be directly resolved, it can be mitigated by having the option to request multiple backend services. These could provide the same information per badge type. Not all research services are available all the time, and not relying on just a single external service improves fault tolerance. Caching might be another way to reduce this effect.
Furthermore, the reliability on the *o2r platform* itself is another issue: *Licence*, *executable*, and *spatial* badges are dependent on an existing *ERC*, which must be linked via DOI to a publication. If a research paper has not been made available as an *ERC* in the *o2r platform*, these badge types will return “n/a” badges indicating no information. The implementation of multiple services per badge type would help with at least one of these (the licence badges): *DOAJ* for example also offers licence information for research publications.

The *o2r-extender* is currently only available for Google Chrome / Chromium. But since Firefox is switching to [WebExtensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions) and slowly moving away from their old “add-ons” completely with [Firefox 57](https://developer.mozilla.org/en-US/Add-ons/Overlay_Extensions/Firefox_addons_developer_guide), a port from a Chrome Extension to the open *WebExtensions* may help making the extender available for more users. There are only minor differences between the two types of extensions. This means the port should be possible with a few changes.

Other steps for further development include:

- Having interactive badges that provide additional information when hovering over them or when the badges are clicked.
- Providing the information in the badges directly via the API in JSON format.
- Supporting more than simple bounding boxes for spatial information.
- Evaluating usage of badges in print applications and for visually impaired people (cf. COS badges)

For more issues see the GitHub issues page for the [o2r-badger](https://github.com/o2r-project/o2r-badger/issues) and [o2r-extender](https://github.com/o2r-project/o2r-extender/issues). Any feedback and ideas are appreciated, either on the GitHub repository or in [this discussion thread](https://groups.google.com/d/topic/reproducible-research/AP0k_xi69AA/discussion) in the Google Group [_Scientists for Reproducible Research_](). We thank the group members for pointing to some of the resources referenced in this post.

## References

- <a name="kidwell"></a>[1] Kidwell, Mallory C., et al. 2016. Badges to Acknowledge Open Practices: A Simple, Low-Cost, Effective Method for Increasing Transparency. <em>PLOS Biology</em> 14(5):e1002456. doi:<a href="https://doi.org/10.1371/journal.pbio.1002456">https://doi.org/10.1371/journal.pbio.1002456</a>.
- <a name="baker"></a>[2] Baker, Monya, 2016. Digital badges motivate scientists to share data. <em>Nature News</em>. doi:<a href="https://doi.org/10.1038/nature.2016.19907">10.1038/nature.2016.19907</a>.
<!-- https://www.nature.com/news/digital-badges-motivate-scientists-to-share-data-1.19907 -->
- <a name="peng1"></a>[4] Peng, Roger D. 2009. Reproducible research and Biostatistics. Biostatistics, Volume 10, Issue 3, Pages 405–408. doi:<a href="https://doi.org/10.1093/biostatistics/kxp014">10.1093/biostatistics/kxp014</a>.
- <a name="peng2"></a>[5] Peng, Roger D. 2011. Reproducible Research in Computational Science. Science 334 (6060): 1226–27. doi:<a href="https://doi.org/10.1126/science.1213847">10.1126/science.1213847</a>.
- <a name="lee"></a>[6] Lee, Duncan, Ferguson, Claire, and Mitchell, Richard. 2009. Air pollution and health in Scotland: a multicity study. Biostatistics, Volume 10, Issue 3, Pages 409–423, doi:<a href="https://doi.org/10.1093/biostatistics/kxp010">10.1093/biostatistics/kxp010</a>.