---
layout: post
title: Writing reproducible manuscripts for Copernicus Publishing's journals
categories:
  - "open science"
  - "reproducible research"
  - "Copernicus"
  - "Copernicus Publishing"
  - "suppdata"
  - "rticles"
author: 'Daniel Nüst'
---

## Reproducibility and transparency in science

The challenges of contemporary science led to widespread calls for more transparency and reproducibility (cf. e.g. Munafò et al., 2017) and promotion of [Open Science](https://en.wikipedia.org/wiki/Open_science) practices, such as Open Data and Open Source.
It can be debated if science really faces a reproducibility crisis (cf. Baker, 2016 and Fanelli, 2018), but the challenges of computer-based research sparked numerous articles (e.g. Sandve et al., 2013, Wilson et al., 2017, Hardwicke et al., 2018, Gil et al., 2016) and drive the development of infrastructure and tools to aide researchers in effectively writing articles, publishing data and code for computations, and communicating their findings in a reproducible way (e.g. Jupyter et al., 2018, ReproZip, 2016, or the concept of [research compendium](https://research-compendium.science/)).

Recent studies showed that the geosciences and GIScience are not beyond issues with reproducibility (Konkol et al., 2018, Nüst et al., 2018, Ostermann & Granell, 2015).
Therefore more and more journals adopt policies on sharing data and code (see Stodden et al., 2018, for a critical evaluation of the effects).
But equally important are an open research culture (Nosek et al., 2015) and teaching researchers so they can adopt more transparent and reproducible workflows, e.g. in courses by _[The Carpentries](https://carpentries.org/)_.
In the light of prevailing issues of a common definition of reproducibility (Barba, 2018), Philip Stark (2018) recently coined the term _preproducibility_ to embrace a positive attitude for more openness and helpfulness.

In the spirit of these activities, this article describes new software releases, which allow the EGU community to write preproducible manuscripts for submission to the large variety of academic journals published by [_Copernicus Publications_](https://www.copernicus.org/).
The new workflow might require hard-earned adjustments for some researchers, but it pays off, especially for early career scientists, because of an increase in transparency and effectivity.
An open and reproducible workflow enables building on others' and own previous work and allows better collaboration to solve the societal challenges of today.

## Reproducible research manuscripts

[Literate programming](https://en.wikipedia.org/wiki/Literate_programming) or digital notebooks are powerful means to improve transparency and preproducibility of research.
[Jupyter Notebook](https://jupyter.org/), [Stencila](http://stenci.la/) or [R Markdown](https://rmarkdown.rstudio.com/) let researchers combine long-form text and source code for analysis and visualisation in a single document.
Text and code are interweaved which makes them easier to grasp, because the are close to each other, and ensures consistency:
each rendering of the document to a desired output format, e.g. PDF, executes the whole workflow (though caching for long-lasting computations is possible).
Authors can transparently expose specific code snippets to readers but also publish the complete source code of the document openly for collaboration and review.

The popular notebook formats are plain text-based, e.g. [Markdown](https://en.wikipedia.org/wiki/Markdown) in case of R Markdown.
Therefore an R Markdown document can be managed with [version control software](https://en.wikipedia.org/wiki/Version_control) for traceability, backup, and online collaboration, e.g. on [GitLab](https://en.wikipedia.org/wiki/GitLab), and stops [the madness of versioning in file names](http://phdcomics.com/comics/archive_print.php?comicid=1531).
R Markdown supports [different programming languages](https://rmarkdown.rstudio.com/lesson-5.html) besides the popular namesake [R](https://www.r-project.org/) and is a sensible solution even if you don't have code in your scholarly manuscript.
It is easy to write, allows you to [manage your bibliography](https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html) effectively, can be rendered to websites as well as PDFs, but most importantly it does not fall short when it is time to submit a manuscript article to a journal.

The [`rticles`](https://cran.r-project.org/package=rticles) extension package for R provides a number of templates for popular journals and publishers.
Since version `0.6` ([published Oct 9 2018](https://github.com/rstudio/rticles/releases/tag/v0.6)) these templates include the [Copernicus Publications Manuscript preparations guidelines for authors](https://publications.copernicus.org/for_authors/manuscript_preparation.html).
The Copernicus Publication staff was kind enough to give a test document a quick review and all seems in order, though of course any problems and questions shall be directed to the software's vibrant community and not the publishers.

The following code snippet and screen shot demonstrate the workflow.
Lines starting with `#` are code comments and explain the steps.

```r
# load required extension packages:
library("rticles")
library("rmarkdown")
# create a new document using a template:
rmarkdown::draft("MyArticle.Rmd", template = "copernicus_article", package = "rticles", edit = FALSE)
# render the source of the document to the default output format:
rmarkdown::render("MyArticle/MyArticle.Rmd")
```

![](/public/images/2018-10_rmd-pdf-example.png)

The commands created a directory with the Copernicus Publishing template's files, including an R Markdown (`.Rmd`) file ready to be edited by you (left-hand side of the screenshot), a [LaTeX](https://en.wikipedia.org/wiki/LaTeX) (`.tex`) file for submission to the publisher, and a `.pdf` file for inspecting the final results and sharing with your colleagues (right hand side of the screenshot).
You can see how simple it is to format text, insert citations, chemical formulas, or equations, and add figures, and how they are rendered into a high-quality output file.

All of these steps may also be completed with user-friendly forms when using [RStudio](https://en.wikipedia.org/wiki/RStudio), a popular development and authoring environment available for all operating systems.
The left hand side of the following screenshot shows the for for creating a new document based on a template, and the right hand side the menu for rendering, called "knitting" with R Markdown because code and text are combined into one document like threads in a garment.

![](/public/images/2018-10_rstudio-ui-example.png)

And in case you decide last minute to submit to a different journal, [`rticles` supports many publishers](https://github.com/rstudio/rticles#overview) so you only have to adjust the template while the whole content stays the same.

## Sustainable access to supplemental data

Scholarly articles receive a digital object identifier ([DOI](https://en.wikipedia.org/wiki/Digital_object_identifier)) for long-term identification and availability.
However, a DOI is not suitable for direct data access, since it points to a human-readable landing page about the identified object.
The R package [`suppdata`](https://cran.r-project.org/package=suppdata) closes this gap (Pearse & Chamberlain, 2018).
It supports downloading supplemental information using the article DOI, and in the latest version the [supported publishers](https://github.com/ropensci/suppdata#supported-publishers-and-repositories) include Copernicus Publications.

The following example code downloads a data file for the article ["Divergence of seafloor elevation and sea level rise in coral reef ecosystems"](https://doi.org/10.5194/bg-14-1739-2017) by Yates et al. published in _Biogeosciences_ in 2017.

```r
# load required extension package:
library("suppdata")
# download a specific supplemental information (SI) file for an article
csv_file <- suppdata::suppdata("10.5194/bg-14-1739-2017",
  si = "Table S1 v2 UFK FOR_PUBLICATION.csv")
# read the data and plot it (toy example!):
my_data <- read.csv(file = csv_file, skip = 3)
plot(x = my_data$NAVD88_G03, y = my_data$RASTERVALU,
  xlab = "Historical elevation (NAVD88 GEOID03))",
  ylab = "LiDAR elevation (NAVD88 GEOID03)",
  main = "A data plot for article 10.5194/bg-14-1739-2017",
  pch = 20, cex = 0.5)
```

<!--
png(file = "public/images/2018-10_suppdata-example-plot.png", width = 512, height = 512, bg = "white")
plot(x = my_data$NAVD88_G03, y = my_data$RASTERVALU,
  xlab = "Historical elevation (NAVD88 GEOID03))",
  ylab = "LiDAR elevation (NAVD88 GEOID03)",
  main = "A silly plot for article 10.5194/bg-14-1739-2017",
  pch = 20, cex = 0.5)
dev.off()
-->

![](/public/images/2018-10_suppdata-example-plot.png)

You can even use this approach in sample code within your paper to make reproductions by reviewers and readers easy and stable, because a publisher can mint a DOI before publication and it will always stay the same.

## Main takeaways

Writing submission-ready manuscripts for Copernicus Publishing's journals just got a lot easier.
Everybody who can write manuscripts with a word processor can learn quickly R Markdown and benefit from a preproducible data science workflow.
Digital notebooks not only improve day-to-day research habits, but are suitable for authoring high-quality scholarly manuscripts and graphics.
The interaction with the publisher is smooth thanks to the LaTeX submission format, but you never have to write any LaTeX.
The workflow is based on an established [Free and Open Source](https://en.wikipedia.org/wiki/Free_and_Open-Source_Software) software stack.
The software is maintained by an active, growing, and welcoming community of researchers and developers with a [strong connection](https://www.r-spatial.org/) to the geospatial sciences.
Because of the complete and consistent notebook, you or a new student can easily pick up the work at a later time (cf. Markowetz, 2015).
The road to effective & transparent research begins with a first step - [take it](https://vickysteeves.gitlab.io/repro-papers/)!

## Acknowledgements

The software updates were contributed by [Daniel Nüst](https://orcid.org/0000-0002-0024-5046) from the project [Opening Reproducible Research](https://o2r.info) (o2r) at the Institute for Geoinformatics, University of Münster, Germany, but would not be able without the support of Copernicus Publishing, the software maintainers most notably [Yihui Xie](https://yihui.name/) and [Will Pearse](htttp://www.pearselab.com/), and the general awesomeness of the R, R-spatial, Open Science, and Reproducible Research communities. Thank you!

## References

<!-- https://crosscite.org/ has a style copernicus-publications -->

- Baker, M.: [1,500 Scientists Lift the Lid on Reproducibility](https://doi.org/10.1038/533452a), Nature, 533(7604), 452–454, doi:10.1038/533452a, 2016. 
- Barba, L. A.: [Terminologies for Reproducible Research](http://arxiv.org/abs/1802.03311), ArXiv:1802.03311 [Cs], February 9, 2018.
- Fanelli, D.: [Opinion: Is Science Really Facing a Reproducibility Crisis, and Do We Need It To?](https://doi.org/10.1073/pnas.1708272114), and do we need it to?, Proceedings of the National Academy of Sciences, 115(11), 2628–2631, doi:10.1073/pnas.1708272114, 2018.
- Gil, Y., David, C. H., Demir, I., Essawy, B. T., Fulweiler, R. W., Goodall, J. L., Karlstrom, L., Lee, H., Mills, H. J., Oh, J.-H., Pierce, S. A., Pope, A., Tzeng, M. W., Villamizar, S. R. and Yu, X.: [Towards the Geoscience Paper of the Future: Best Practices for Documenting and Sharing Research from Data to Software to Provenance](https://doi.org/10.1002/2015EA000136), Earth and Space Science, 3(10), 388–415, doi:10.1002/2015ea000136, 2016. 
- Hardwicke, T. E., Mathur, M. B., MacDonald, K., Nilsonne, G., Banks, G. C., Kidwell, M. C., Hofelich Mohr, A., Clayton, E., Yoon, E. J., Henry Tessler, M., Lenne, R. L., Altman, S., Long, B. and Frank, M. C.: [Data availability, reusability, and analytic reproducibility: evaluating the impact of a mandatory open data policy at the journal Cognition](https:://doi.org/10.1098/rsos.180448), Royal Society Open Science, 5(8), 180448, doi:10.1098/rsos.180448, 2018.
- Konkol, M. and Kray, C.: [In-depth examination of spatiotemporal figures in open reproducible research](https:://doi.org/10.1080/15230406.2018.1512421), Cartography and Geographic Information Science, 1–16, doi:10.1080/15230406.2018.1512421, 2018. 
- Konkol, M., Kray, C. and Pfeiffer, M.: [Computational reproducibility in geoscientific papers: Insights from a series of studies with geoscientists and a reproduction study](https:://doi.org/10.1080/13658816.2018.1508687), International Journal of Geographical Information Science, 1–22, doi:10.1080/13658816.2018.1508687, 2018. 
- Markowetz, F.: [Five selfish reasons to work reproducibly](https:://doi.org/10.1186/s13059-015-0850-7), Genome Biology, 16(1), doi:10.1186/s13059-015-0850-7, 2015. 
- Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J. and Ioannidis, J. P. A.: [A manifesto for reproducible science, Nature Human Behaviour](https:://doi.org/10.1038/s41562-016-0021), 1(1), 21, doi:10.1038/s41562-016-0021, 2017. 
- Nüst, D., Granell, C., Hofer, B., Konkol, M., Ostermann, F. O., Sileryte, R. and Cerutti, V.: [Reproducible research and GIScience: an evaluation using AGILE conference papers](https:://doi.org/10.7717/peerj.5072), PeerJ, 6, e5072, doi:10.7717/peerj.5072, 2018. 
- Ostermann, F. O. and Granell, C.: [Advancing Science with VGI: Reproducibility and Replicability of Recent Studies using VGI](https:://doi.org/10.1111/tgis.12195), Transactions in GIS, 21(2), 224–237, doi:10.1111/tgis.12195, 2016. 
- Pearse, W. D. and A Chamberlain, S.: [Suppdata: Downloading Supplementary Data from Published Manuscripts](https:://doi.org/10.21105/joss.00721), Journal of Open Source Software, 3(25), 721, doi:10.21105/joss.00721, 2018. 
- [ReproZip: Computational Reproducibility With Ease](https://osf.io/vc72z/), F. Chirigati, R. Rampin, D. Shasha, and J. Freire. In Proceedings of the 2016 ACM SIGMOD International Conference on Management of Data (SIGMOD), pp. 2085-2088, 2016
- Sandve, G. K., Nekrutenko, A., Taylor, J. and Hovig, E.: [Ten Simple Rules for Reproducible Computational Research](https:://doi.org/10.1371/journal.pcbi.1003285), edited by P. E. Bourne, PLoS Computational Biology, 9(10), e1003285, doi:10.1371/journal.pcbi.1003285, 2013. 
- Jupyter, P., Bussonnier, M., Forde, J., Freeman, J., Granger, B., Head, T., Holdgraf, C., Kelley, K., Nalvarte, G., Osheroff, A., Pacer, M., Panda, Y., Perez, F., Ragan-Kelley, B. and Willing, C.: [Binder 2.0 - Reproducible, interactive, sharable environments for science at scale](http://conference.scipy.org/proceedings/scipy2018/pdfs/project_jupyter.pdf), in Proceedings of the 17th Python in Science Conference, SciPy., 2018. 
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L. and Teal, T. K.: [Good enough practices in scientific computing, edited by F. Ouellette](https:://doi.org/10.1371/journal.pcbi.1005510), PLOS Computational Biology, 13(6), e1005510, doi:10.1371/journal.pcbi.1005510, 2017.
- Yates, K. K., Zawada, D. G., Smiley, N. A. and Tiling-Range, G.: [Divergence of seafloor elevation and sea level rise in coral reef ecosystems](https://doi.org/10.5194/bg-14-1739-201), Biogeosciences, 14(6), 1739–1772, doi:10.5194/bg-14-1739-2017, 2017.
