---
layout: post
title: "Beyond o2r: collaborations and community activity for more open and reproducible science"
author: "Daniel Nüst"
layout: post
categories:
  - transparency
  - open science
  - reproducibility
  - AGILE
  - CODECHECK
---

The o2r project has its primary goals in providing tools to enhance scholarly communication.
We build technology to help solving relevant problems.
With the Executable Research Compendium and supporting software, we provide a different, more holistic take on how research output should look like in the future, especially if data and software are involved in the scientific workflow.
However, tech is not all we do and o2r team members actively work with the GIScience community and the broader scientific community.
This blog post briefly introduces two recent collaborations that are less about technology and more about community, culture, and people.
<!--more-->
## 1. Citable and preserved AGILE short papers

We're a big fan of the AGILE conference: we have [organised](/2017/05/10/o2r-at-AGILE/) [several](/2018/06/21/agile-2018-pre-conference-workshop-report/) [workshops](/2019/07/01/AGILE-2019-Limassol/), contributed to [stocktacking the reproducibility of AGILE conference publications](https://doi.org/10.7717/peerj.5072), and co-authored the [AGILE Reproducible Paper Guidelines](https://doi.org/10.17605/OSF.IO/CB7Z8).
These activites are collected under the umbrella of [_Reproducible AGILE_](https://reproducible-agile.github.io/):

[![Reproducible AGILE logo](https://reproducible-agile.github.io/public/images/reproducible-AGILE-logo-square.svg){:width="200px"}](https://reproducible-agile.github.io/)

The AGILE conference features a full paper and a short paper track.
The _full paper proceedings 2020_ are [published as Open Access (yay!) with Copernicus](https://www.agile-giscience-series.net/), which is a huge step towards more accessibility and openness in the community.
Because of the cancellation of the conference, there are no _short paper proceedings_ in 2020.

However, the **short papers** up to 2019 are published as so called ["bronze Open Access"](https://en.wikipedia.org/wiki/Open_access#Bronze_OA), meaning that they are published on a website and can be downloaded, but the license is unclear.
The the question of preservation is not properly answered either, and referencing AGILE short papers is not possible up to today's standards because they lack a unique identifier.
This is a huge shame, because, having published a few AGILE short papers, I know that the peer review process is solid and very helpful especially for ideas in an early stage.
Furthermore, short papers are often written by early career researchs (in fact, my first ever scientific publication as first author was [at AGILE 2010](https://eartharxiv.org/jq5df/)).

That is why I reached out to the [AGILE council](https://agile-online.org/agile-community/council) and suggested to add a statement to the [AGILE proceedings website](https://agile-online.org/conference/proceedings), which clearly gives authors the permission to re-publish or ["self-archive"](https://en.wikipedia.org/wiki/Self-archiving) the short paper PDFs in a proper repository.
My initiative was triggered by a concrete event: one of my AGILE short papers was not accepted by my favourite preprint server [EarthArXiv](https://eartharxiv.org/) (which also hosts postprints, see also [on Wikipedia](https://en.wikipedia.org/wiki/EarthArXiv)) because it was not clear I had permission to submit a paper that was previously published elsewhere.
This is a very reasonable [moderation policy](https://eartharxiv.github.io/moderation.html), and the interaction with EarthArXiv advisory council member [Allison Enright](https://www.unb.ca/faculty-staff/directory/science-fr-earth/enright-allison.html) in the matter was extremely nice and helpful.
After providing some good arguments via email and some endurance, I was very happy to learn that the council followed my suggestion and added the following statement to [the proceedings website](https://agile-online.org/conference/proceedings/):

> _Authors have permission to deposit AGILE short papers, published in the proceedings below and available as PDFs on the server https://agile-online.org, in a public repository, such as a preprint server or institutional repositories._
> _Authors may only use repositories that provide a DOI for the published record._
> 
> _Authors are strongly encouraged, and may be required by repositories e.g. EarthArXiv (https://eartharxiv.org/), to add a cover page to the uploaded PDF._
> _The cover page should include name, time and place of the conference, the URL to the conference website, and a statement that the short paper is peer reviewed._
> _If possible, authors should add the tags or keywords 'AGILE short paper' and 'AGILEGIS' and configure the recommended citation to include year and name of the conference._

How this all played out confirmed my trust and apprecciation for the EarthArXiv and AGILE communities.

**Did you author an AGILE short paper in the past?**
Please help to preserve the knowledge of the GIScience community.
You can do it today!
Find step-by-step instructions and some more background here: **[https://reproducible-agile.github.io/short-paper-postprints/](https://reproducible-agile.github.io/short-paper-postprints/)**
It really just takes 5 minutes.

<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">AGILE <a href="https://twitter.com/hashtag/AGILEGIS?src=hash&amp;ref_src=twsrc%5Etfw">#AGILEGIS</a> short papers can now be self-archived/deposited in institutional repositories or preprint servers (recommendation:👉<a href="https://twitter.com/EarthArXiv?ref_src=twsrc%5Etfw">@EarthArXiv</a> ♥️🌎🌍🌏♥️):<a href="https://t.co/FiRd5YWEDJ">https://t.co/FiRd5YWEDJ</a><br><br>Preserve your work now! (and ensure others can cite you properly...) <a href="https://twitter.com/hashtag/postprint?src=hash&amp;ref_src=twsrc%5Etfw">#postprint</a> <a href="https://twitter.com/hashtag/OpenAccess?src=hash&amp;ref_src=twsrc%5Etfw">#OpenAccess</a> <a href="https://t.co/j3lNAMC8tU">pic.twitter.com/j3lNAMC8tU</a></p>&mdash; Daniel Nüst (@nordholmen) <a href="https://twitter.com/nordholmen/status/1273642585639333889?ref_src=twsrc%5Etfw">June 18, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## 2. CODECHECK

o2r has an [approach and goals](/about/) grounded in the belief that technology can help to reduce barriers for reproducibility and make benefits of reproducible publications more readily available to the broad diversity of geoscientific researchers.
Our focus lies in packaging code (scripts, runtime environment), data, and documentation together (the [ERC](/erc-spec/)) and integrate it into peer review and the scholarly publication process (our [pilots](/pilots/)).

While these goals and approach are true, and start to come to fruition, one can also take a completely different approach.
Enter [_CODECHECK_](https://codecheck.org.uk/).

[![](https://codecheck.org.uk/img/codecheck_logo.svg){:width="200px"}](https://codecheck.org.uk/)

CODECHECK is a joint initiative by Daniel Nüst and [Stephen J. Eglen](https://sje30.github.io/), reader in Computational Neuroscience at the University of Cambridge.
Daniel and Stephen were brought together by failure: both applied for a small Open Science grant with the Wellcome trust, but both were rejected.
Luckily, they both took advantage of the option to publish their project proposals, so they could see they had similar ideas.
Also starting out as technology driven, CODECHECK has developed into something completely different from o2r.

To introduce better recognition of computational workflows in the peer review process, Stephen and Daniel developed a set of [four _principles](https://codecheck.org.uk/#the-codecheck-principles).
Based on these principles, scientific journals or the community can build a process, of which [many variants are imaginable](https://codecheck.org.uk/process/), for executing code and data-based workflows during peer review.

1. Codecheckers record but don’t investigate or fix.
1. Communication between humans is key.
1. Credit is given to codecheckers.
1. Workflows must be auditable.

These principles embrace openness ideals and the opportunity to introduce early career researchers and research software developers in peer review.
Instead of trying to preserve and package everything, CODECHECK transfers the gist of peer reviewing articles to code execution: at one point in time, one fellow researcher or developer was able to execute a given worklow following the provided instructions.
Some see this as a low bar, I see it as an option to break the current stagnancy of code review in science (see also the [CODECHECK FAQs](https://codecheck.org.uk/faq)).

The currently most active implementation of these principles is the [community process](https://codecheck.org.uk/guide/community-process), but the first successes of CODECHECKs conducted as part of journal publications are also already completed and the number of volunteering codecheckers is slowly rising.
Stephen put in a lot of effort to contribute to the scientific knowledge by codechecking coronavirus simulations, which not only strengthens trust in science but lead to a nice [Nature News article](https://doi.org/10.1038/d41586-020-01685-y).
Please check out the CODECHECK website and the [CODECHECK register](https://codecheck.org.uk/register/) for details, and see [how you can get involved](https://codecheck.org.uk/get-involved/) as author, reviewer, or journal editor.

------

## _Low tech, community work, and technological advances go hand in hand in Opening Reproducible Research._
