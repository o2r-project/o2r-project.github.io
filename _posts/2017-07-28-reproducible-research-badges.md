---
layout: post
title: Reproducible Research Badges
categories:
  - badges
  - research
  - chrome extension
author: 'Lukas Lohoff, Daniel Nüst'
---

*This blog post is based on work started in the study project [Badges for computational geoscience containers](https://zivgitlab.uni-muenster.de/geocontainer-badges) at [ifgi](https://www.uni-muenster.de/Geoinformatics/). We thank the [project team](https://github.com/o2r-project/o2r-badger#contributors) for their great work!*

## Introduction

Today badges are widely used in open source software repositories. They have a high recognition value and consequently provide an easy and efficient way to convey basic metadata such as version numbers, build status, download count, or container image size. Now imagine similar badges not for software projects but for modern research: We developed a backend service that provides badges for reproducible research papers to answer questions such as: 

- When was a research paper published?
- Is it openly accessible?
- Was the paper published in a peer reviewed journal?
- What is the research location i.e. the location where the data is from?
- Can the results be reproduced?

We are not the first nor the only ones to do this: [ScienceOpen](https://www.scienceopen.com/) already has badges for open access publications, content type, views, comments and [Altmetric](https://www.altmetric.com/) score:

![scienceopen badges](/public/images/2017-07-28-badges/scienceOpen.png "Figure 1: ScienceOpen badges")

These are helpful when using the ScienceOpen website, but they’re not available for other websites. Additional issues are the four different styles and that some relevant information for reproducible geosciences is not available, e.g. executability status or the research location.

Badges are also used directly for publications, leaving out the search engine “middleman”. Usually the published document, poster or presentation contains a badge along with the information needed to access the data or code. For example, the [Center for Open Science](https://cos.io/) [designed badges](https://osf.io/tvyxz/wiki/home/) for scientific articles. University of Washington’s [eScience Institute](http://escience.washington.edu/) created a peer-review process for open data and open materials badges (https://github.com/uwescience-open-badges/about) based on the COS badges. The service is meant for faculty members and students at the University of Washington, but even external researchers can apply. They also have a great list of [publications on the topic](https://github.com/uwescience-open-badges/about#where-can-i-read-more-about-this).

A study [[1](#kidwell)] by Mallory C. Kidwell et. al. demonstrates that introducing such open data badges had a positive effect in the *Psychological Science* journal: After the journal started awarding badges for open data, more articles stated open data availability. The. They see badges as a simple yet effective way to promote data publishing. 

Although these two examples are limited to a specific journal or institution respectively, they demonstrate the potential impact of badges. That is why our goal is to explore sophisticated and novel badge types (reproducibility, research location, etc.) and to find out how to provide them independently from a specific journal, conference, or website.

## o2r-badger

Advanced badges to answer the above questions come in handy when doing literature research as they open new ways of exploring research. But how can we get the required information for these badges? Some of these questions, such as the publication date, the peer review status and the open access status, can already be answered by online research library APIs, i.e. [Crossref](https://www.crossref.org/) or DOAJ[https://doaj.org/]. The [o2r API](http://o2r.info/o2r-web-api/) can (or will be able to) answer the remaining questions about reproducibility and location: Knowing if a publication is reproducible is a core part of this project. Furthermore, the location on which a research paper focuses, is extracted using o2r-meta (https://github.com/o2r-project/o2r-meta) by analyzing spatial files in the workspace of the publication. How can we integrate the information from these different sources?

o2r-badger (https://github.com/o2r-project/o2r-badger) is a Node.js application. It provides an API endpoint based on the [Express](https://expressjs.com/) web application framework. The API serves badges for reproducible research with information from multiple online services and has routes for five different badge types:

- `/badge/executable/:id`
- `/badge/licence/:id`
- `/badge/spatial/:id`
- `/badge/peerreview/:id`
- `/badge/releasetime/:id`

The badger currently provides two kinds of badges: internally created SVG-based badges, and redirects to [shields.io](https://shields.io/). The SVG-based badges are called extended badges and often contain more precise information: the extended license badge for example has three categories (code, data and text) of openness compared to just a single value in the standard shields.io badge. 

![license badge](/public/images/2017-07-28-badges/license_extended.svg "Figure 2: An extended licence badge reporting open data, text and code")

Extended badges are meant for posters or websites that focus on a single publication. They can even be resized and provided as an PNG image using the API parameters. See the badger [API documentation](https://github.com/o2r-project/o2r-badger#api-documentation-version-02) for more info. Meanwhile the standard shields.io badges are much smaller, yet still contain most of the important information:

![shields.io badge](https://img.shields.io/badge/licence-open-44cc11.svg)
 
They excel at applications where space is important, for example search engines that list many research articles. [Shields.io](https://shields.io/) generates these SVG images on the fly when you request a URL (e.g. `https://img.shields.io/badge/licence-open-44cc11.svg`) in which you specify the text (`licence` and `open`) and the color (`44cc11` is a [HTML color code](http://html-color-codes.info/) for green). Thanks to them for providing their services free of charge!

How do you make use of these badges? Firstly, they are ready to be integrated into other projects or websites. Let’s look at an example of an *executable* badge. Simply request the badge from the badger instance on the o2r server by providing the DOI of the publication for the `:id` element in the above routes, for example

https://o2r.uni-muenster.de/api/1.0/badge/executable/10.1126%2Fscience.1092666

This URL requests a badge for the reproducibility status of the paper “Global Air Quality and Pollution” from *[Science](http://science.sciencemag.org/)* magazine identified by the DOI [10.1126/science.1092666](https://doi.org/10.1126/science.1092666). When the request is sent, the following steps will happen:

1. The badger tries to find a research paper inside the o2r platform, called Executable Research Compendium ([ERC](http://o2r.info/erc-spec/spec/)) with the given DOI
2. If if finds an ERC, it looks for a matching *[job](http://o2r.info/o2r-web-api/job/)*, a report of a reproduction analysis.
3. Depending on the reproduction result (`success`, `running`, or `failure`) specified in the job, the badger generates a green, yellow or red badge with matching text indicating the reproducibility of the specified research publication.
4. The request is redirected to a [shields.io](https://shields.io/) URL link containing the color and textual information. If an extended badge is requested, the badger generates and sends a SVG graphic instead.

The returned image contains the requested information, which is in this case a successful reproduction:

https://img.shields.io/badge/executable-yes-44cc11.svg

Badges for reproducibility, peer review status and license are color coded to provide additional visual aids indicating for example (un)successful reproducibility.

While a common procedure is reused across the badge types, other badges are generated with different functions and get their information from other sources. The information for peer review and releasetime badges is requested from the external services DOAJ and Crossref. The spatial badge also uses the o2r services, but it additionally converts the spatial information from coordinates into textual information, i.e. place names, using the [Geonames API](http://www.geonames.org/export/web-services.html). 

## Spread badges over the web

So there is a great badge server, and databases providing manifold badge information, but how to get them displayed online? The sustainable way would be for research website operators to agree on a common badge system and design, and then incorporate these badges on their platforms. But we know that is never ever going to happen, so instead of waiting we created a chrome extension for common research websites. The o2r-extender (https://github.com/o2r-project/o2r-extender) automatically inserts badges into search results or publication pages using client-side browser scripting. Its available in the Chrome Web Store (*[here](https://chrome.google.com/webstore/detail/opening-reproducible-rese/fhhfncpkfohlhphlcgpkbpialfhkmbil)*)  and ready to be tried out.

The extender currently supports the following websites:

- Google Scholar (https://scholar.google.de/)
- DOAJ.org (https://doaj.org/)
- ScienceDirect.com (http://www.sciencedirect.com/)
- ScienceOpen.com (https://scienceopen.com/)
- PLOS.org (https://www.plos.org/)
- Microsoft Academic (https://academic.microsoft.com/)
- Mendeley (https://www.mendeley.com/)

For each listed article contained in these research websites, the extender requests a set of badges from the o2r-badger. These are then inserted into the page’s HTML code after rendering the regular website:

![google scholar badges](/public/images/2017-07-28-badges/google_scholar_badges.png "Figure 3: Badges integrated into Google Scholar search results")

When the badger does not find information for a certain DOI, it returns a grey “not available” - badge instead, as shown in the screenshot above for the outermost license and peer review badges. 

The extender consists of a content script, similar to a [userscript](http://techsupportguides.com/what-is-a-userscript/), for each research website. The content scripts insert a set of badges (Figure 3) for each article in the respective website. They all use a set of base functions defined in the chrome extension for generating HTML, getting DOIs and inserting badges.

The listed results on each website can also be filtered based on badge values, and selected badge types can be turned on or off directly from the website with controls, which are also inserted into the page (see Figure 4). Results not matching the filter or articles where the DOI could not be detected are greyed out.

![doaj filtering](/public/images/2017-07-28-badges/doaj_badges.png "Figure 4: Filtering search results on DOAJ")


### Configuration

The extender is easily configurable: it can be enabled and disabled with a simple click on the icon in the browser toolbar. You can select the badge types to be displayed in the extension settings. Additionally it contains links to local info pages (“Help” and “About”), explaining the extender and the different badge types:

![extender config](/public/images/2017-07-28-badges/extender_configuration.png "Figure 5: o2r-extender configuration")

## Outlook: Action integrations

The extender also has a feature that has nothing to do with badges at all. In the context of open science and reproducible research, we have place the reproducibility service in a larger context as described in the [o2r architecture](http://o2r.info/architecture/) (see section Business context). Two core aspects are loading research workspaces from cloud storage and connecting to suitable data repositories for actual storage of ERCs.

To facilitate this integration for users, the extender can also augment the user interfaces  of the cloud collaboration platform [Sciebo](http://sciebo.de/) and the scientific data repository [Zenodo](https://zenodo.org/) to integrate our reproducibility service.

When using Sciebo, a button is added  to a file’s or directory’s context menu. It allows direct submission of workspaces to the o2r platform to create a new Executable Research Compendium (ERC): 

![sciebo integration](/public/images/2017-07-28-badges/sciebo_integration.png "Figure 6: Sciebo upload integration")

On the other hand, when you are viewing an Executable Research Compendium on Zenodo, a small badge redirects to the inspection view in the o2r platform:

![zenodo integration](/public/images/2017-07-28-badges/zenodo_integration.png "Figure 7: Zenodo inspection integration")

## Challenges

The study project [Badges for computational geoscience containers](https://zivgitlab.uni-muenster.de/geocontainer-badges) initially implemented eight microservices responsible for the six different badges types, badge scaling and testing. A microservice architecture using Docker containers was not chosen because the project needs immense scaling capabilities, but for another reason: developing independent microservices makes work organization much easier, especially for a study project where students prefer different programming languages and have different skillsets. However, for the o2r project, the eight microservices needed to become a single microservice. This required refactoring, rewriting and bug fixing. Now, when a badge is requested, a [promise chain](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) is called depending on the badge type. It consists of a number of functions of which some are used by all badges. The functions each contain code written in the study project separated into small chunks to avoid a [callback hell](http://callbackhell.com/).
In the extender, a critical feature is the detection of the DOI just from a research paper title. For some websites such as DOAJ.org or ScienceOpen.com this is not necessary, as they provide the DOI directly for each entry. But when the DOI is not directly provided, the extender tries to get the DOI from a request to CrossRef.org. This is not alway successful or may find incorrect results depending on the paper title.
As discussed above, in an ideal world the o2r-extender Chrome extension would not be necessary. A “hacky” solutions is not always a bad solution, but there are a few tricky parts with a workaround like this: The extension is supporting nine different websites. If there are changes to one of these, the extender has to be updated as well. For example, [Sciebo](http://sciebo.de/), an [OwnCloud](https://owncloud.org/) implementation, recently changed their URLs to include a “fileid” parameter which resulted in an error when parsing the current folder path.

## Future Work

There is still potential for future improvements: one of the biggest current issues is the reliability on external services such as Crossref and DOAJ. While this issue cannot be directly resolved, it can be mitigated by having the option to request multiple backend services, which could provide the same information per badge type. Not all research services are available all the time, and not relying on just a single external service improves fault tolerance. Caching might be another way to reduce this effect.
Furthermore, the reliability on the o2r platform itself is another issue: *Licence*, *executable*, and *spatial* badges are dependent on an existing ERC, which must be linked via DOI to a publication. If a research paper has not been made available as an ERC in the o2r platform, these badge types will return “n/a” badges indicating no information. The implementation of multiple services per badge type would help with at least one of these (the licence badges) as DOAJ also offers licence information for research publications.

The o2r-extender is currently only available for Google Chrome / Chromium. But since Firefox is switching to [WebExtensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions) and slowly moving away from their old “Addons” completely with [Firefox 57](https://developer.mozilla.org/en-US/Add-ons/Overlay_Extensions/Firefox_addons_developer_guide), a port from a Chrome Extension to the open WebExtensions may help making the extender available for more users. There are only minor differences between the two types of extensions, which means the port should be possible with a few changes.

Other issues include:

- Having interactive badges that provide additional information when hovering over them or when the badges are clicked.
- Providing the information in the badges directly via the API in JSON format.
- Supporting more than simple bounding boxes for spatial information.

## <a name="kidwell"></a> References

\[1] Kidwell, Mallory C., et al. 2016 Badges to Acknowledge Open Practices: A Simple, Low-Cost, Effective Method for Increasing Transparency. *PLOS Biology* 14(5):e1002456. DOI: https://doi.org/10.1371/journal.pbio.1002456  