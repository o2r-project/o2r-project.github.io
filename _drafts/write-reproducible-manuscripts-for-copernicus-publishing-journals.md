---
layout: post
title: Write reproducible manuscripts for Copernicus Publishing's journals
categories:
  - "open science"
  - "reproducible research"
  - "Copernicus"
  - "Copernicus Publishing"
  - "suppdata"
  - "rticles"
author: 'Daniel Nüst'
---

The need to increase computational reproducibility in science is hardly debated anymore.
Instead, the scientific community puts efforts into education and improving toolboxes and the o2r project is proud to be part of such an important and active field in research.
This blog post introduces the changes made by o2r team member [Daniel](https://twitter.com/nordholmen) to two R packages to establish a reproducible research workflow for manuscripts submitted to [o2r external parter](https://o2r.info/about/#external-partners) [_Copernicus Publications_](https://www.copernicus.org/).

**Reproducible research manuscripts**

[Literate programming](https://en.wikipedia.org/wiki/Literate_programming), or notebooks, is seen as a powerful concept to improve transparency and reproducibility of research.
Tools such as [Jupyter Notebook](https://jupyter.org/), [Stencila](http://stenci.la/) or [R Markdown](https://rmarkdown.rstudio.com/) allow researchers to combine long-form text and code in a single document.

<span style="color: red;">TODO: three screenshots of example notebooks for each tool.</span>

The data analyses and visualisations are close to the computational instructions which generate them.
Authors can transparently expose specific code to readers but also publish the complete source code of the document openly.
Popular notebook formats are plain text-based, e.g. [Markdown](https://en.wikipedia.org/wiki/Markdown) in case of R Markdown, so they can be managed with [version control software](https://en.wikipedia.org/wiki/Version_control) and allow online collaboration, e.g. on [GitLab](https://en.wikipedia.org/wiki/GitLab).
R Markdown supports [different programming languages](https://rmarkdown.rstudio.com/lesson-5.html), allows you to easily [manage your bibliography](https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html), and is a sensible solution even if you don't have code in your manuscript because Markdown is much easier to grasp as a beginner than LaTeX.
There is no need to track which version of the code or input parameters generated the final plot that should end up in a manuscript, because all computations are executed when the notebook is compiled into a different file format for publication, e.g. HTML or PDF (using [LaTeX](https://en.wikipedia.org/wiki/LaTeX) behind the curtains but [easily configurable](https://bookdown.org/yihui/rmarkdown/pdf-document.html#latex-packages-for-citations)).
Learn more about such a workflow in the EGU 2018 short course ["Writing reproducible geoscience papers using R Markdown, Docker and GitLab"](https://vickysteeves.gitlab.io/repro-papers/).

_How can researchers arrange their modern reproducible workflow with journal requirements?_
The [`rticles`](https://cran.r-project.org/package=rticles) package to the rescue!
It provides a number of templates for popular journals and publishers, and since version `0.6` ([published Oct 9 2018](https://github.com/rstudio/rticles/releases/tag/v0.6)) these templates include the [Copernicus Publications Manuscript preparations guidelines for authors](https://publications.copernicus.org/for_authors/manuscript_preparation.html).
While the package is maintained by [Yihui Xie](https://yihui.name/) and the template was contributed by Daniel, the Copernicus staff was kind enough to give a test document a quick review and all seems in order.
Note that Coperncius cannot give you support with code or R Markdown, but please to hesitate to get in touch with Daniel if you encounter any issues concerning the template.

You can tell R Markdown to keep the intermediate LaTex files when rendering to PDF.
The following code snippet demonstrates the workflow:

```r
#install.packages(c("rticles", "rmarkdown"))
> library("rticles")
> library("rmarkdown")
> rmarkdown::draft("MyArticle.Rmd", template = "copernicus_article", package = "rticles", edit = FALSE)
> rmarkdown::render("MyArticle/MyArticle.Rmd")
> list.files("MyArticle")
 [1] "copernicus.bst"          "copernicus.cfg"
 [3] "copernicus.cls"          "MyArticle.pagelist"
 [5] "MyArticle.pdf"           "MyArticle.Rmd"
 [7] "MyArticle.tex"           "Nikolaus_Kopernikus.jpg"
 [9] "pdfscreencop.sty"        "sample.bib"
```

As you can see in the file listing, the commands created a directory with the Copernicus Publishing template's files, an `.Rmd` file ready to be edited by you, a `.tex` file for submission, and a `.pdf` file for sharing with your colleagues.
The latter looks as follows:

<span style="color: red;">TODO: screenshots of created PDF</span>

Try it out and take a look at the created R Markdown file.
You can quickly see how simple it is to format the text and insert citations while the format lets you focus on the content.
The Open Source software stack used by R Markdown, e.g. [pandoc](https://pandoc.org/) and LaTex, takes care of creating high-quality output files.

**DOI-based supplemental data access**

Articles as well as data sets published today typically receive a [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) for long-term identification and availability.
However, a DOI is not suitable for direct data access, since it points to a human-readable landing page.
Luckily, and unsurprisingly, there is an R package to help with that:
[`suppdata`](TODO: link here) aids downloading data from published papers.
To download the supplementary data file from an article published in a Copernicus Publishing journal, you can simply type:

```r
#install.packages("suppdata")
> library("suppdata")
> cop_unzipped_files <- suppdata("10.5194/bg-14-1739-2017", si = 1)
> list.files(cop_unzipped_files)
[1] "bg-14-1739-2017-supplement-title-page.pdf"
[2] "bg-20160407-Yates-major revision supplementary methods-FOR_PUBLICATION.docx"
[3] "Table S1 v2 UFK FOR_PUBLICATION.csv"
[4] "Table S2 v2 LFK FOR_PUBLICATION.csv"
[5] "Table S3 v2 STT FOR_PUBLICATION.csv"
[6] "Table S4 v2 STC FOR_PUBLICATION.csv"
[7] "Table S5 v2 Maui FOR_PUBLICATION.csv"
[8] "Table S6 FOR_PUBLICATION.docx"
```

You can even access a specific file from the supplement (which always is a `.zip`-file for this publisher) and directly start using it.

```r
> csv_file <- suppdata("10.5194/bg-14-1739-2017", si = "Table S1 v2 UFK FOR_PUBLICATION.csv")
> my_data <- read.csv(file = csv_file, skip = 3)
> library("skimr")
> skim(my_data) # excerpt shown only!
Skim summary statistics
 n obs: 26341
 n variables: 9

── Variable type:integer ───────────────────────────────────────────────────────
 variable missing complete     n    mean  sd   p0  p25  p50  p75 p100     hist
     YEAR       0    26341 26341 1934.55 0.5 1934 1934 1935 1935 1935 ▆▁▁▁▁▁▁▇

── Variable type:numeric ───────────────────────────────────────────────────────
   variable missing complete     n       mean       sd         p0        p25
 RASTERVALU       0    26341 26341      -6.72     2.91     -21.54      -8.61
    Zchange       0    26341 26341      -0.13     0.78      -8.25      -0.44
         p50        p75       p100     hist
      -6.17       -4.44      -0.97 ▁▁▁▁▃▆▇▂
      -0.086       0.24       6.46 ▁▁▁▁▇▁▁▁
```

`suppdata` supports [other journals](TODO), too.
Because the publisher can mint a DOI before publication, you can even use this approach in the samples within your paper!

**Important takeaways**

Writing submission ready articles for Copernicus Publishing's journals just got a lot easier.
Everybody who can write manuscripts with a word processor can learn R Markdown and benefit from a reproducible data science ''workflow and an established Open Source software stack for authoring high quality documents.
And if your analysis runs in R, you can write code that easily accesses an article's supplemental files for full transparency.  

Further down the road, we see the updates introduced todays as building blocks towards complete transparency with an integrated publication of text, data, and as [research compendia](https://research-compendium.science/), and easy interaction and reproduction with [executable research compendia](https://doi.org/10.1045/january2017-nuest) (ERC).
Try out the [o2r demo server](https://o2r.info/results/) to learn more about the possibilities of ERCs.
