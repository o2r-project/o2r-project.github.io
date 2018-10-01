---
layout: post
title: "Demo server update"
categories:
  - demo
  - "reproducible research"
  - "reproducibility service"
  - implementation
author: 'Daniel Nüst'
---

We've been working on demonstrating our [reference-implementation](/results) during spring an managed to create a number of example workspaces.
We now decided to publish these workspaces on [our demo server](https://o2r.uni-muenster.de/).

[![o2r screenshot 1: listing of compendia](/public/images/2018-08-14-demo/o2r-demo-listing.jpg "Screenshot 1: o2r reference implementation listing of published ERC"){:width="600"}](https://o2r.uni-muenster.de/)
<p class="attributionInlineImage">Screenshot 1: o2r reference implementation <em>listing of published Executable Research Compendia</em>. The right-hand side shows a metadata summary including original authors.</p>

The papers were originally published in <!--more--> [Journal of Statistical Software](https://www.jstatsoft.org/) or in a [Copernicus Publications](https://publications.copernicus.org/) journal under open licenses.
We have created an R Markdown document for each paper based on the included data and code following the [ERC specification](https://o2r.info/erc-spec/spec/) for naming core files, but only included data, an R Markdown document and a HTML display file.
The publication metadata, the runtime environment description (i.e. a `Dockerfile`), and the runtime image (i.e. a Docker image tarball) were all created during the ERC creation process without any human interaction (see the used [R code for upload](https://github.com/o2r-project/erc-examples/blob/master/corpus/showcases.Rmd)), since required metadata were included in the R Markdown document's front matter.

The documents include selected figures or in some cases the whole paper, if runtime is not extremely long.
While the paper's authors are correctly linked in the workspace metadata (see right hand side in _Screenshot 1_), the "o2r author" of all papers is o2r team member Daniel since he made the uploads.
You can find all publications on his author page (this is the link you definitely want to try out!):

❗ **[https://o2r.uni-muenster.de/#!/author/0000-0002-0024-5046](https://o2r.uni-muenster.de/#!/author/0000-0002-0024-5046)** ❗

![o2r screenshot 2: example compendium view](/public/images/2018-08-14-demo/o2r-demo-compendium.jpg "Screenshot 2: o2r reference implementation display of a single ERC"){:width="600"}
<p class="attributionInlineImage">Screenshot 2: o2r reference implementation <em>ERC detail page</em> for compendium [SLVlQ](https://o2r.uni-muenster.de/#!/erc/5LVlQ). The link "Article" in the top left corner leads to the original article, the "magnifying glass" button takes you to a core feature: the reproduction result.</p>

You can get to the original publication by clicking the "Article" button in the top left corner (see _Screenshot 2_).
The workspaces demonstrate a variety of issues and are a great source for future work on architecture and implementation.
Here are some examples of the power of a reproducible research service and publishing platform:

- The [ERC for "Tidy Data" by Hadley Wickham](https://o2r.uni-muenster.de/#!/erc/N4Jzp) completes the reproduction successfully, so no differences between the uploaded and reproduced HTML file were found! You can even download the image tarball (just bear with our demo - not production - server it it takes some time).
- The [ERC for "A question driven socio-hydrological modeling process" by Garcia et al.](https://o2r.uni-muenster.de/#!/erc/Z4Hci) "fails" due to differences in the created figure. A human can now judge if these differences are minor, or the author can try to tweak rendering parameters to fix this. <bf />![o2r screenshot 3: image difference example](/public/images/2018-08-14-demo/o2r-demo-imagediff.jpg "Screenshot 3: image difference example of "failed" replication"){:width="400"}
- A [demo ERC with randomised output](https://o2r.uni-muenster.de/#!/erc/IKnWD) shows how things can really go wrong. Feel free to click "Run Analysis" and see how the differences changes with each execution.

If you want to go through the creation process yourself, register on the platform (this requires a short manual interaction by us) and upload one of selected workspaces, which you can find in our public demo share at [https://uni-muenster.sciebo.de/s/G8vxQ1h50V4HpuA](https://uni-muenster.sciebo.de/s/G8vxQ1h50V4HpuA) (just look for zip files starting with `corpus_..`).
Please take care to choose appropriate licenses and be aware that we might remove compendia from the demo platform without prior notice.

We welcome _your feedback_ [on Twitter](https://twitter.com/o2r_project/status/1029293814756851712), in the [reference implementation GitHub project](https://github.com/o2r-project/reference-implementation/issues/13), or in the comments below.
