---
layout: post
title: Investigating Docker and R
categories:
  - introduction
  - overview
  - R
  - Docker
author: 'Daniel Nüst'
---

_This post is regularly updated (cf. [GH issue](https://github.com/o2r-project/o2r-project.github.io/issues/10)) and available under the URL **[http://bit.ly/docker-r](http://bit.ly/docker-r)**. Last update: 22 Aug 2017._

Docker and R: How are they used and could they be used together?
That is the question that we regularly ask ourself. And we try to keep up with other people's work! In this post, we are going to share our insights with you.

![Docker loves R, R loves Docker](/public/images/docker-loves-r.png "Docker loves R, R loves Docker"){:width="400"}

_Thanks to [Ben Marwick](http://faculty.washington.edu/bmarwick/) for [contributing](https://github.com/o2r-project/o2r-project.github.io/pull/6) to this post! You know about a project using Docker and R? [Get in touch](https://github.com/o2r-project/o2r-project.github.io/issues/new)._

## Dockerizing R

Several implementations of besides the one by R-core exist today, together with numerous integrations into open source and proprietary software (cf. [Englisch](https://en.wikipedia.org/wiki/R_(programming_language)#Implementations) and [German](https://de.wikipedia.org/wiki/R_(Programmiersprache)#Alternative_Open-Source-Interpreter) Wikipedia pages). In the following we present the existing efforts for using _open source_ R implementation with Docker.

### Rocker

The most prominent effort<!--more--> in this area is the **Rocker project**. It was initiated by [Dirk Eddelbuettel](http://dirk.eddelbuettel.com/) and [Carl Boettiger](http://www.carlboettiger.info/) and containerizes the main R implementation. For an introduction, you may read their blog post [here](http://dirk.eddelbuettel.com/blog/2014/10/23/) or follow [this tutorial](http://ropenscilabs.github.io/r-docker-tutorial/) from rOpenSci.

![Rocker logo](/public/images/rocker-logo.png "Rocker logo"){:width="200" .img.rightfloat}

With a big choice of pre-build Docker images, Rocker provides optimal solutions for those who want to run R from Docker containers. Explore it on [Github](https://github.com/rocker-org/) or [Docker Hub](https://hub.docker.com/u/rocker/), and soon you will find out that it takes just one single command to run instances of either [base R](https://hub.docker.com/r/rocker/r-base/), [R-devel](https://hub.docker.com/r/rocker/r-devel/) or [Rstudio Server](https://hub.docker.com/r/rocker/rstudio/). Moreover, you can run [previous versions of R](https://hub.docker.com/r/rocker/r-versioned/) or use one of the many bundles with commonly used R packages and other software (e.g. bundles going back to [Hadley Wickham](https://hub.docker.com/r/rocker/hadleyverse/) and [rOpenSci](https://hub.docker.com/r/rocker/ropensci/)).

Images are build monthly on Docker Hub, except _devel_ tags which are build nightly, but not on every push but triggered by CRON jobs running on a third party server (cf. [GitHub comment](https://github.com/rocker-org/rocker-versioned/issues/42#issuecomment-316149983)).

### Bioconductor

If you come from Bioinformatics or neighboring disciplines, you might be delighted that [**Bioconductor**](http://bioconductor.org/) provides several images based on Rocker's `rocker/rstudio` images (see the [help page](http://bioconductor.org/help/docker/), [GitHub](https://github.com/Bioconductor/bioc_docker), and [Open Hub](https://hub.docker.com/u/bioconductor/)). Image updates occur with each Bioconductor release, except the _devel_ images which are build weekly with the latest versions of R and Bioconductor based on `rocker/rstudio-daily`.

### MRO

![MRO logo](/public/images/mro-logo.png "MRO logo (C) Microsoft"){:width="150" .img.rightfloat}

Microsoft R Open ([MRO](https://mran.revolutionanalytics.com/open)) is an "enhanced R distrubition", formerly known as Revolution R Open (RRO) before [Revolution Analytics](https://en.wikipedia.org/wiki/Revolution_Analytics) was acquired by Microsoft. MRO is compatible with main R and it's packages. "It includes additional capabilities for improved performance, reproducibility, and platform support." ([source](https://mran.revolutionanalytics.com/rro/)); most notably these are the [MRAN repository](http://mran.revolutionanalytics.com/) a.k.a. CRAN Time Machine, which is also used by versioned Rocker images, and the (optional) integration with [Intel® Math Kernel Library](https://software.intel.com/en-us/mkl) (MKL) for [multi-threaded performance](https://mran.revolutionanalytics.com/documents/rro/multithread) in linear algebra operations ([BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) and [LAPACK](https://en.wikipedia.org/wiki/LAPACK)).

o2r team member Daniel created a Docker image for MRO inkluding MKL. It is available [on Docker Hub](https://hub.docker.com/r/nuest/mro/) as `nuest/mro`, with [Dockerfile on GitHub](https://github.com/nuest/mro-docker).
It is inspired by the Rocker images and can be used in the same fashion. Please note the extended licenses printed at every startup for MKL.

### Renjin

![Renjin logo](/public/images/renjin-logo-v4.svg "Renjin logo"){:width="150" .img.rightfloat}

[Renjin](http://www.renjin.org/about.html) is a [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine)-based interpreter for the R language for statistical computing developed by [BeDataDriven](http://www.bedatadriven.com/). It was developed for big data analysis using existing R code seamlessly in cloud infrastructures, and allows Java/Scala developers to easily combine R with all benefits of Java and the JVM.

While it is not primarily build for interactive use on the command line, this is possible. So o2r team member Daniel created a Docker image for Renjin for you to try it out. It is available [on Docker Hub](https://hub.docker.com/r/nuest/renjin/) as `docker pull nuest/renjin`, with [Dockerfile on GitHub](https://github.com/nuest/renjin-docker).


## Dockerizing Research and Development Environments

So why, apart from the incredibly easy usage, adoption and transfer of typical R environments, would you want to combine R with Docker?

Ben Marwick, Associate Professor at the University of Washington, explains in [this presentation](https://benmarwick.github.io/UW-eScience-docker-for-reproducible-research/) that it helps you manage dependencies. It gives a computational environment that is isolated from the host, and at the same time transparent, portable, extendable and reusable. Marwick uses Docker and R for **reproducible research** and thus bundles up his works to a kind of *Research Compendium*; an instance is available [here](https://github.com/benmarwick/1989-excavation-report-Madjebebe), and a template [here](https://github.com/benmarwick/researchcompendium).

[![Screenshot Boettiger ACM paper](/public/images/boettiger-acm.jpg "Screenshot Boettiger ACM paper"){:width="150" .img.rightfloat}](https://doi.org/10.1145/2723872.2723882)

Carl Boettiger, Assistant Professor at UC Berkeley, has also written in detail about using Docker for reproducibility in his ACM SIGOPS paper ['An introduction to Docker for reproducible research, with examples from the R environment'](https://doi.org/10.1145/2723872.2723882).

Both Ben and Carl have written about their case studies using Docker for research compendia in the book ["The Practice of Reproducible Research - Case Studies and Lessons from the Data-Intensive Sciences"](https://www.gitbook.com/book/bids/the-practice-of-reproducible-research/details): [Using R and Related Tools for Reproducible Research in Archaeology](https://www.practicereproducibleresearch.org/case-studies/benmarwick.html) and [A Reproducible R Notebook Using Docker](https://www.practicereproducibleresearch.org/case-studies/cboettig.html).

An R extension you may want to dockerize is **Shiny**. Flavio Barros dedicated two articles on R-bloggers to this topic: [Dockerizing a Shiny App](https://www.r-bloggers.com/dockerizing-a-shiny-app/) and [Share Shiny apps with Docker and Kitematic](https://www.r-bloggers.com/share-your-shiny-apps-with-docker-and-kitematic/).
The majority of talks at [useR!2017](https://user2017.brussels) presenting [real-world deployments of Shiny](https://user2017.brussels/schedule) mentioned using Dockerized Shiny applications for scalability and ease of installation.

A new solution to ease the creation of Docker containers for specific research environments is [the package <code>containerit</code>](https://github.com/o2r-project/containerit).
It creates Dockerfiles (using Rocker base images) from R sessions, R scripts, RMarkdown files or R workspace directories, including the required system dependencies.
The package was [presented at useR!2017](http://o2r.info/2017/07/07/useR2017) and can currently be installed from GitHub.

## Running Tests

The R package [**dockertest**](https://github.com/traitecoevo/dockertest) makes use of the isolated environment that Docker provides: R programmers can set up test environments for their R packages and R projects, in wich they can rapidly test their works on Docker containers that only contain R and the relevant dependencies. All of this without cluttering your development environment.

## Dockerizing Documents

Some works are dedicated to _dockerizing R-based documents_. The [**liftr package**](http://liftr.me/) for R lets users enhance Rmd files with YAML-metadata, wich enables rendering R Markdown documents in Docker containers. Liftr also supports [Rabix](https://www.rabix.org/), a Docker-based toolkit for portable bioinformatics workflows. That means that users can have Rabix workflows run inside the container and have the results integrated directly into the final document. 

## Controll Docker Containers from R

Rather than running R inside Docker containers, it can be beneficial to call Docker containers from inside R. This is what the packages `RSelenium` and `googleComputeEngineR` do.

[**Selenium**](http://www.seleniumhq.org/) provides tools for browser automation, which are also [available as Docker images](https://hub.docker.com/u/selenium/). They can be used, amongst others, for testing web applications or controlling a headless web browser from your favorite programming language. In [this tutorial](https://rpubs.com/johndharrison/RSelenium-Docker), you can see how and why you should use RSelenium to interact with your Selenium containers.

[**googleComputeEngineR**](https://cloudyr.github.io/googleComputeEngineR/) provides an R interface to the Google Cloud Compute Engine API. It includes a function called `docker_run` that starts a Docker container in a Google Cloud VM and executes R code in it. Read [this article](https://cloudyr.github.io/googleComputeEngineR/articles/docker-ssh-futures.html) for details and examples. There are similar ambitions to implement Docker capabilities in the [**analogsea package**](https://github.com/sckott/analogsea) that interfaces the Digital Ocean API.

`googleComputeEngineR` and `analogsea` use functions from the [**harbor package**](https://github.com/wch/harbor/) for R. You should have a look at it, because it may help you to control your own Docker containers that run either locally or remotely.

## R and Docker for Complex Web Applications

Docker, in general, may help you to build complex and scalable web applications with R. 

Mark McCahill presented at [an event](https://sites.duke.edu/researchcomputing/2014/09/23/duke-docker-day-was-great/) of the Duke University in North Carolina (USA) how he provided 300+ students each with private RStudio Server instances. In his presentation ([PDF](https://sites.duke.edu/researchcomputing/files/2014/09/mccahill-DockerDays.pdf) / [MOV](https://people.duke.edu/~mdelong/mccahill-DockerDays.mov) (398 MB)), he explains his **RStudio farm** in detail. 

If you want to use **RStudio with cloud services**, you may find delight in these articles from the SAS and R blog: [RStudio in the cloud with Amazon Lightsail and docker](http://sas-and-r.blogspot.de/2016/12/rstudio-in-cloud-with-amazon-lightsail.html), [Set up RStudio in the cloud to work with GitHub](http://sas-and-r.blogspot.de/2016/01/set-up-rstudio-in-cloud-to-work-with.html), [RStudio in the cloud for dummies, 2014/2015 edition](http://sas-and-r.blogspot.de/2014/12/rstudio-in-cloud-for-dummies-20142015.html).

The platform [**R-hub**](https://github.com/r-hub) helps R developers with solving package issues prior to submitting them to CRAN. In particular, it provides services that build packages on all CRAN-supported platforms and checks them against the latest R release. The services utilize backends that perform regular R builds inside of Docker containers. Read the [project proposal](https://github.com/r-hub/proposal) for details.
