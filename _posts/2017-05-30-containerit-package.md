---
layout: post
title: Generating Dockerfiles for reproducible research with R
categories:
  - thesis
  - theses
  - research
author: 'Daniel Nüst, Matthias Hinz'
meta-json: '{"date":"2017-05-30","output":{"md_document":{"variant":"markdown\\_mmd","toc":true,"toc_depth":"2"}},"author":"Matthias Hinz, Daniel Nüst", "title":"Generating Dockerfiles for reproducible research with R","vignette":"%\\VignetteEngine{knitr::rmarkdown}\n%\\VignetteIndexEntry{Generating Dockerfiles for reproducible research with R}\n%\\VignetteEncoding{UTF-8}"}'
---

_This post is the draft of the vignette for a new R package by o2r team members [Matthias](https://github.com/MatthiasHinz) and [Daniel](https://github.com/nuest). Find the original file [in the package repository on GitHub](https://github.com/o2r-project/containerit/blob/master/vignettes/containerit.Rmd)._

-   [1. Introduction](#introduction)
-   [2. Creating a Dockerfile](#creating-a-dockerfile)
-   [3. Including resources](#including-resources)
-   [4. Image metadata](#image-metadata)
-   [5. Further customization](#further-customization)
-   [6. CLI](#cli)
-   [7. Challenges](#challenges)
-   [8. Conclusions and future work](#conclusions-and-future-work)
-   [Metadata](#metadata)

## 1. Introduction

Even though R is designed for open and reproducible research, users who
want to share their work with others are facing challenges. Sharing
merely the R script or R Markdown document should warrant
reproducibility, but many analyses rely on additional resources and
specific third party software as well. An R script may <!--more-->produce
unexpected results or errors when executed under a different version of
R or another platform. Reproduciblility is only assured by providing
complete setup instructions and resources. Long-term reproducibility can
be achieved by either regular maintenance of the code, i.e. keeping it
always working with the latest package versions from CRAN. It can be
supported by packages such as
[packrat](https://rstudio.github.io/packrat/) and platforms such as
[MRAN](https://mran.microsoft.com/), which provide means to capture a
specific combination of R packages. An alternative to updating or
managing packages explicitly is providing the full runtime environment
in its original state, using [virtual
machines](https://en.wikipedia.org/wiki/Virtual_machine) or [software
containers](https://en.wikipedia.org/wiki/Operating-system-level_virtualization).

The R extension package `containerit` aims to facilitate the latter
approach by making reproducible and archivable research with containers
easier. The development is supported by the DFG-funded project Opening
Reproducible Research (o2r, <http://o2r.info>). `containerit` relies on
[Docker](http://docker.com/) and automatically generates a container
manifest, or "recipe", with setup instructions to recreate a runtime
environment based on a given R session, R script, R Markdown file or
workspace directory. The resulting
[`Dockerfile`](https://docs.docker.com/engine/reference/builder/) can
not only be read and understood by humans, but also be interpreted by
the Docker engine to create a software container containing all the R
packages and their system dependencies. This way all requirements of an
R workflow are packaged in an executable format.

The created Dockerfiles are based on the
[Rocker](https://github.com/rocker-org/rocker) project ([Rocker on
Docker Hub](https://hub.docker.com/u/rocker/),
[introduction](http://dirk.eddelbuettel.com/blog/2014/10/23/#introducing_rocker)).
Using the stack of version-stable Rocker images, it is possible to match
the container's R version with the local R installation or any R version
the user requires. `containerit` executes the provided input workspace
or file first locally on the host machine in order to detect all
dependencies. For determining external software dependencies of attached
packages, `containerit` relies (a) on the [sysreqs
database](https://sysreqs.r-hub.io/) and makes use of the corresponding
web API and R package, and (b) on internally defined rule sets for
challenging configurations.

The Dockerfile created by `containerit` can then be used to build a
Docker image. Running the image will start an R session that closely
resembles the creating systems runtime environment. The image can be
shared and archived and works anywhere with a compatible Docker version.

To build images and run containers, the package integrates with the
[harbor](https://github.com/wch/harbor) package and adds a few
convenience functions for interacting with Docker images and containers.
For concrete details on reading, loading, or installing the *exact*
versions of R packages including their system dependencies/libraries,
this project focuses on the geospatial domain. `containerit` uses the
package
[`futile.logger`](https://cran.r-project.org/web/packages/futile.logger/)
to provide information to the user at a configurable level of detail,
see [futile.logger
documentation](https://cran.r-project.org/web/packages/futile.logger/README.html).

In the remainder of this vignette, we first introduce the main usage
scenarios for `containerit` and document current challenges as well as
directions for future work.

## 2. Creating a Dockerfile

### 2.1 Basics

The easiest way to generate a Dockerfile is to run an analysis in an
interactive R session and create a Dockerfile for this session by
loading `containerit` and calling the `dockerfile()`- method with
default parameters. As shown in the example below, the result can be
pretty-printed and written to a file. If no `file` argument is supplied
to `write()`, the Dockerfile is written to the current working directory
as `./Dockerfile`, following the typical naming convention of Docker.

When packaging any resources, it is essential that the R working
directory is the same as the build context, to which the Dockerfile
refers. All resources must be located below this directory so that they
can be refered to by relative paths (e.g. for copy instructions). This
must also be considered when packaging R scripts that use relative
paths, e.g. for reading a file or sourcing another R script.

### 2.2 Packaging an interactive session

    library("containerit")

    ## 
    ## Attaching package: 'containerit'

    ## The following object is masked from 'package:base':
    ## 
    ##     Arg

    # do stuff, based on demo("krige")
    library("gstat")
    library("sp")

    data(meuse)
    coordinates(meuse) = ~x+y
    data(meuse.grid)
    gridded(meuse.grid) = ~x+y
    v <- variogram(log(zinc)~1, meuse)
    m <- fit.variogram(v, vgm(1, "Sph", 300, 1))
    plot(v, model = m)

    # create Dockerfile representation
    dockerfile_object <- dockerfile()

    ## INFO [2017-05-30 14:49:20] Trying to determine system requirements for the package(s) 'sp, gstat, knitr, Rcpp, intervals, lattice, FNN, spacetime, zoo, digest, rprojroot, futile.options, backports, magrittr, evaluate, stringi, futile.logger, xts, rmarkdown, lambda.r, stringr, yaml, htmltools' from sysreq online DB
    ## INFO [2017-05-30 14:49:21] Adding CRAN packages: sp, gstat, knitr, Rcpp, intervals, lattice, FNN, spacetime, zoo, digest, rprojroot, futile.options, backports, magrittr, evaluate, stringi, futile.logger, xts, rmarkdown, lambda.r, stringr, yaml, htmltools
    ## INFO [2017-05-30 14:49:21] Created Dockerfile-Object based on sessionInfo

The representation of a Dockerfile in R is an instance of the S4 class
`Dockerfile`.

    dockerfile_object

    ## An object of class "Dockerfile"
    ## Slot "image":
    ## An object of class "From"
    ## Slot "image":
    ## [1] "rocker/r-ver"
    ## 
    ## Slot "postfix":
    ## An object of class "Tag"
    ## [1] "3.4.0"
    ## 
    ## 
    ## Slot "maintainer":
    ## An object of class "Label"
    ## Slot "data":
    ## $maintainer
    ## [1] "daniel"
    ## 
    ## 
    ## Slot "multi_line":
    ## [1] FALSE
    ## 
    ## 
    ## Slot "instructions":
    ## [[1]]
    ## An object of class "Run_shell"
    ## Slot "commands":
    ## [1] "export DEBIAN_FRONTEND=noninteractive; apt-get -y update"
    ## [2] "apt-get install -y pandoc \\\n\tpandoc-citeproc"         
    ## 
    ## 
    ## [[2]]
    ## An object of class "Run"
    ## Slot "exec":
    ## [1] "install2.r"
    ## 
    ## Slot "params":
    ##  [1] "-r 'https://cloud.r-project.org'" "sp"                              
    ##  [3] "gstat"                            "knitr"                           
    ##  [5] "Rcpp"                             "intervals"                       
    ##  [7] "lattice"                          "FNN"                             
    ##  [9] "spacetime"                        "zoo"                             
    ## [11] "digest"                           "rprojroot"                       
    ## [13] "futile.options"                   "backports"                       
    ## [15] "magrittr"                         "evaluate"                        
    ## [17] "stringi"                          "futile.logger"                   
    ## [19] "xts"                              "rmarkdown"                       
    ## [21] "lambda.r"                         "stringr"                         
    ## [23] "yaml"                             "htmltools"                       
    ## 
    ## 
    ## [[3]]
    ## An object of class "Workdir"
    ## Slot "path":
    ## [1] "/payload/"
    ## 
    ## 
    ## 
    ## Slot "cmd":
    ## An object of class "Cmd"
    ## Slot "exec":
    ## [1] "R"
    ## 
    ## Slot "params":
    ## [1] NA

The printout below shows the rendered Dockerfile. Its instructions
follow a pre-defined order:

1.  define the base image
2.  define the maintainer label
3.  install system dependencies and external software
4.  install the R packages themselves
5.  set the working directory
6.  copy instructions and metadata labels (see examples in
    later sections)
7.  `CMD` instruction (final line) defines the default command when
    running the container

Note that the maintainer label as well as the R version of the base
image are detected from the runtime environment, if not set to different
values manually.

    print(dockerfile_object)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
     && apt-get install -y pandoc \
        pandoc-citeproc
    RUN ["install2.r", "-r 'https://cloud.r-project.org'", "sp", "gstat", "knitr", "Rcpp", "intervals", "lattice", "FNN", "spacetime", "zoo", "digest", "rprojroot", "futile.options", "backports", "magrittr", "evaluate", "stringi", "futile.logger", "xts", "rmarkdown", "lambda.r", "stringr", "yaml", "htmltools"]
    WORKDIR /payload/
    CMD ["R"]

Instead of printing out to the console, you can also write to a file:

    write(dockerfile_object, file = tempfile(fileext = ".dockerfile"))

    ## INFO [2017-05-30 14:49:21] Writing dockerfile to /tmp/Rtmp25OKLi/file1a9726e56459.dockerfile

### 2.3 Packaging an external session

Packaging an interactive session has the disadvantage that unnecessary
dependencies might be added to the Dockerfile and subsequently to the
container. For instance the package `futile.logger` is a dependency of
`containerit`, and it will be added to the container because it was
loaded into the same session were the analyses was executed. It cannot
be removed by default, because other packages in the session *might* use
it as well (even unintentionally in case of generic methods). Therefore,
it is safer not to tamper with the current session, but to run the
analysis in an isolated *vanilla* session, which does not have
`containerit` in it. The latter will batch-execute the commands in a
seperate instance of R and retrieves an object of class `sessionInfo`.
The session info is then used as input to `dockerfile()`. This is also
how `dockerfile()` works internally when packaging either expressions,
scripts or R markdown files.

The following code creates a Dockerfile for a list of expressions in a
vanilla session.

    exp <- c(expression(library(sp)),
             expression(data(meuse)), 
             expression(mean(meuse[["zinc"]])))
    session <- clean_session(exp, echo = TRUE)

    ## INFO [2017-05-30 14:49:21] Creating an R session with the following arguments:
    ##   R  --silent --vanilla -e "library(sp)" -e "data(meuse)" -e "mean(meuse[[\"zinc\"]])" -e "info <- sessionInfo()" -e "save(list = \"info\", file = \"/tmp/Rtmp25OKLi/rdata-sessioninfo1a9714893e92\")"

    dockerfile_object <- dockerfile(from = session)

    ## INFO [2017-05-30 14:49:23] Trying to determine system requirements for the package(s) 'sp, lattice' from sysreq online DB
    ## INFO [2017-05-30 14:49:24] Adding CRAN packages: sp, lattice
    ## INFO [2017-05-30 14:49:24] Created Dockerfile-Object based on sessionInfo

    print(dockerfile_object)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    RUN ["install2.r", "-r 'https://cloud.r-project.org'", "sp", "lattice"]
    WORKDIR /payload/
    CMD ["R"]

### 2.4 Packaging an R script

R scripts are packaged by just supplying the file path or paths to the
arguement `from` of `dockerfile()`. They are automatically copied into
the container's working directory. In order to run the R script on
start-up, rather than an interactive R session, a CMD instruction can be
added by providing the value of the helper function `CMD_Rscript()` as
an argument to `cmd`.

    # create simple script file
    scriptFile <- tempfile(pattern = "containerit_", fileext = ".R")
    writeLines(c('library(rgdal)',
                 'nc <- rgdal::readOGR(system.file("shapes/", package="maptools"), "sids", verbose = FALSE)',
                 'proj4string(nc) <- CRS("+proj=longlat +datum=NAD27")',
                 'plot(nc)'), scriptFile)

    # use a custom startup command
    scriptCmd <- CMD_Rscript(basename(scriptFile))

    # create Dockerfile for the script
    dockerfile_object <- dockerfile(from = scriptFile, silent = TRUE, cmd = scriptCmd)

    print(dockerfile_object)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
     && apt-get install -y gdal-bin \
        libgdal-dev \
        libproj-dev
    RUN ["install2.r", "-r 'https://cloud.r-project.org'", "rgdal", "sp", "lattice"]
    WORKDIR /payload/
    COPY [".", "."]
    CMD ["R", "--vanilla", "-f", "containerit_1a977e2dcdea.R"]

### 2.5 Packaging an R Markdown file

Similarly to scripts, R Markdown files can be passed to the `from`
argument. In the following example, a vignette from the Simple Features
package `sf` is packaged in a container. To render the document at
startup, the Dockerfile's `CMD` instruction must be changed. To do this,
the `cmd` argument passed to `dockerfile()` is constructed using the
function `CMD_Render`. Note that, as shown in the Dockerfile, the GDAL
library has to be build from source for `sf` to work properly, because a
quite recent version of GDAL is required. This adaptation of the
installation instruction is based on an internal ruleset for the package
`sf`.

    response <- file.copy(from = system.file("doc/sf3.Rmd",package = "sf"),
                            to = temp_workspace, recursive = TRUE)
    vignette <- "sf3.Rmd"

    dockerfile_object <- dockerfile(from = vignette, silent = TRUE, cmd = CMD_Render(vignette))

    ## Loading required namespace: sf

    print(dockerfile_object)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
     && apt-get install -y gdal-bin \
        libgeos-dev \
        libproj-dev \
        libudunits2-dev \
        make \
        pandoc \
        pandoc-citeproc \
        wget
    WORKDIR /tmp/gdal
    RUN wget http://download.osgeo.org/gdal/2.1.3/gdal-2.1.3.tar.gz \
     && tar zxf gdal-2.1.3.tar.gz \
     && cd gdal-2.1.3 \
     && ./configure \
     && make \
     && make install \
     && ldconfig \
     && rm -r /tmp/gdal
    RUN ["install2.r", "-r 'https://cloud.r-project.org'", "dplyr", "sf", "Rcpp", "assertthat", "digest", "rprojroot", "R6", "DBI", "backports", "magrittr", "evaluate", "units", "rlang", "stringi", "rmarkdown", "udunits2", "stringr", "yaml", "htmltools", "knitr", "tibble"]
    WORKDIR /payload/
    COPY ["sf3.Rmd", "sf3.Rmd"]
    CMD ["R", "--vanilla", "-e", "rmarkdown::render(\"sf3.Rmd\", output_format = rmarkdown::html_document())"]

### 2.6 Packaging a workspace directory

A typical case expected to be interesting for `containerit` users is
packaging a local directory with a collection of data and code files. If
providing a directory path to the `dockerfile()` function, the package
searches for the first occurence of an R script, or otherwise the first
occurence of an R markdown file. It then proceeds to package this file
along with all other resources in the directory, as shown in the next
section.

## 3. Including resources

Analyses in R often rely on external files and resources that are
located located in the workspace. When scripts or R markdown files are
packaged, they are copied by default into the same location relative to
the working directory. The argument `copy` influences how `dockefile()`
behaves in this matter. It can either have the values `script` (default
behaviour), `script_dir` (copies the complete directory in which the
input file is located), or a custom list of files and directories inside
the current working directory

    response <- file.copy(from = system.file("simple_test_script_resources/", 
                                             package = "containerit"),
                          to = temp_workspace, recursive = TRUE)


    dockerfile_object <- dockerfile("simple_test_script_resources/",
                  copy = "script_dir",
                  cmd = CMD_Rscript("simple_test_script_resources/simple_test.R"))

    print(dockerfile_object)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    WORKDIR /payload/
    COPY ["simple_test_script_resources", "simple_test_script_resources/"]
    CMD ["R", "--vanilla", "-f", "simple_test_script_resources/simple_test.R"]

Including R objects works similar to resources, using the argument
`save_image`. The argument can be set to `TRUE` to save *all* objects of
the current workspace to an .RData file, which is then copied to the
container's working directory and loaded on startup (based on
`save.image()`).

    df <- dockerfile(save_image = TRUE)
    print(df)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
     && apt-get install -y gdal-bin \
        libgeos-dev \
        libproj-dev \
        libudunits2-dev \
        make \
        pandoc \
        pandoc-citeproc \
        wget
    WORKDIR /tmp/gdal
    RUN wget http://download.osgeo.org/gdal/2.1.3/gdal-2.1.3.tar.gz \
     && tar zxf gdal-2.1.3.tar.gz \
     && cd gdal-2.1.3 \
     && ./configure \
     && make \
     && make install \
     && ldconfig \
     && rm -r /tmp/gdal
    RUN ["install2.r", "-r 'https://cloud.r-project.org'", "sp", "gstat", "knitr", "Rcpp", "magrittr", "units", "lattice", "rjson", "FNN", "udunits2", "stringr", "xts", "DBI", "lambda.r", "futile.logger", "htmltools", "intervals", "yaml", "rprojroot", "digest", "sf", "futile.options", "evaluate", "rmarkdown", "stringi", "backports", "spacetime", "zoo"]
    WORKDIR /payload/
    COPY ["./.RData", "./"]
    CMD ["R"]

Alternatively, a object names as well as other arguments can be passed
as a list, which then are passed to the `save()` function.

    require(fortunes)

    ## Loading required package: fortunes

    rm(list = ls())
    calculation <- 41 + 1
    frtn <- fortunes::fortune()
    original_sessionInfo <- sessionInfo()

    df <- dockerfile(silent = TRUE,
                     save_image = list("original_sessionInfo", "frtn"))

    print(df)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="daniel"
    RUN export DEBIAN_FRONTEND=noninteractive; apt-get -y update \
     && apt-get install -y gdal-bin \
        libgeos-dev \
        libproj-dev \
        libudunits2-dev \
        make \
        pandoc \
        pandoc-citeproc \
        wget
    WORKDIR /tmp/gdal
    RUN wget http://download.osgeo.org/gdal/2.1.3/gdal-2.1.3.tar.gz \
     && tar zxf gdal-2.1.3.tar.gz \
     && cd gdal-2.1.3 \
     && ./configure \
     && make \
     && make install \
     && ldconfig \
     && rm -r /tmp/gdal
    RUN ["install2.r", "-r 'https://cloud.r-project.org'", "fortunes", "sp", "gstat", "knitr", "Rcpp", "magrittr", "units", "lattice", "rjson", "FNN", "udunits2", "stringr", "xts", "DBI", "lambda.r", "futile.logger", "htmltools", "intervals", "yaml", "rprojroot", "digest", "sf", "futile.options", "evaluate", "rmarkdown", "stringi", "backports", "spacetime", "zoo"]
    WORKDIR /payload/
    COPY ["./payload.RData", "./payload.RData"]
    CMD ["R"]

## 4. Image metadata

Metadata can be added to Docker images using [Label
instructions](https://docs.docker.com/engine/reference/builder/#label).
Label instructions are key-value pairs of arbitrary content. A dublicate
key overwrites existing ones. Although it is up to the user how many
labels are created, it is recommended to bundle them into one Label
instruction in the Dockerfile. Each use of the `Label()` function
creates a seperate instruction in the Dockerfile.

As shown in section 2, the maintainer label is set by default to the top
as the dockerfile and contains the username of the current host system.
The maintainer can be changed with the `maintainer` argument of
`dockerfile()`:

    labeled_dockerfile <- dockerfile(from = clean_session(), maintainer = "Jon_Doe@example.com")

Labels can be applied to the existing Dockerfile object using the
`addInstructions()` function, which adds any newly created instructions
to the end of the Dockerfile but before the CMD statement. The `Label()`
constructor can be used for creating labels of arbitrary content and
works similar to creating named lists in R.

    # A simple label that occupies one line:
    label1 <- Label(key1 = "this", key2 = "that", otherKey = "content")
    addInstruction(labeled_dockerfile) <- label1

    #label with fixed namespace for all keys
    label2 <- Label("name"="A name", "description" = "A description", label_ns = "my.label.ns.")

    # A multiline label with one key/value pair per line
    label3 <- Label("info.o2r.name" = "myProject_ImageName", "org.label-schema.name"="ImageName", 
                    "yet.another_labelname"="true", multi_line = TRUE)
    addInstruction(labeled_dockerfile) <- list(label2, label3)

Metadata according to the [Label Schema](http://label-schema.org/rc1/)
conventions can be created with a function constructed by the helper
factory `LabelSchemaFactory()`.

    Label_LabelSchema <- LabelSchemaFactory()
    label <- Label_LabelSchema(name = "ImageName", description = "Description of the image", build_date = Sys.time())
    addInstruction(labeled_dockerfile) <- label

You can also put session information, using either base R or `devtools`,
into a label as plain text or as json:

    addInstruction(labeled_dockerfile) <- Label_SessionInfo(session = clean_session())
    addInstruction(labeled_dockerfile) <- Label_SessionInfo(session = devtools::session_info(), as_json = TRUE)

The resulting Dockerfile with all the labels:

    print(labeled_dockerfile)

    FROM rocker/r-ver:3.4.0
    LABEL maintainer="Jon_Doe@example.com"
    WORKDIR /payload/
    LABEL key1="this" key2="that" otherKey="content"
    LABEL my.label.ns.name="A name" my.label.ns.description="A description"
    LABEL info.o2r.name="myProject_ImageName" \
        org.label-schema.name="ImageName" \
        yet.another_labelname="true"
    LABEL org.label-schema.schema-version="1.0.0-rc.1" \
        org.label-schema.build-date="2017-05-30T14:49:39+0200" \
        org.label-schema.name="ImageName" \
        org.label-schema.description="Description of the image"
    LABEL R.session-info="R version 3.4.0 (2017-04-21)\nPlatform: x86_64-pc-linux-gnu (64-bit)\nRunning under: Ubuntu 16.04.2 LTS\n\nMatrix products: default\nBLAS: /usr/lib/libblas/libblas.so.3.6.0\nLAPACK: /usr/lib/lapack/liblapack.so.3.6.0\n\nlocale:\n [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              \n [3] LC_TIME=en_GB.UTF-8        LC_COLLATE=en_US.UTF-8    \n [5] LC_MONETARY=en_GB.UTF-8    LC_MESSAGES=en_US.UTF-8   \n [7] LC_PAPER=en_GB.UTF-8       LC_NAME=C                 \n [9] LC_ADDRESS=C               LC_TELEPHONE=C            \n[11] LC_MEASUREMENT=en_GB.UTF-8 LC_IDENTIFICATION=C       \n\nattached base packages:\n[1] stats     graphics  grDevices utils     datasets  methods   base     \n\nloaded via a namespace (and not attached):\n[1] compiler_3.4.0"
    LABEL R.session-info="{\"platform\":{\"version\":\"R version 3.4.0 (2017-04-21)\",\"system\":\"x86_64, linux-gnu\",\"ui\":\"X11\",\"language\":\"en\",\"collate\":\"en_US.UTF-8\",\"tz\":\"Europe/Berlin\",\"date\":\"2017-05-30\"},\"packages\":{\"package\":[\"backports\",\"base\",\"compiler\",\"containerit\",\"datasets\",\"DBI\",\"devtools\",\"digest\",\"evaluate\",\"FNN\",\"fortunes\",\"futile.logger\",\"futile.options\",\"graphics\",\"grDevices\",\"grid\",\"gstat\",\"htmltools\",\"intervals\",\"knitr\",\"lambda.r\",\"lattice\",\"magrittr\",\"memoise\",\"methods\",\"Rcpp\",\"rjson\",\"rmarkdown\",\"rprojroot\",\"sf\",\"sp\",\"spacetime\",\"stats\",\"stringi\",\"stringr\",\"tools\",\"udunits2\",\"units\",\"utils\",\"withr\",\"xts\",\"yaml\",\"zoo\"],\"*\":[\"\",\"*\",\"\",\"*\",\"*\",\"\",\"\",\"\",\"\",\"\",\"*\",\"\",\"\",\"*\",\"*\",\"\",\"*\",\"\",\"\",\"*\",\"\",\"\",\"\",\"\",\"*\",\"\",\"\",\"\",\"\",\"\",\"*\",\"\",\"*\",\"\",\"\",\"\",\"\",\"\",\"*\",\"\",\"\",\"\",\"\"],\"version\":[\"1.0.5\",\"3.4.0\",\"3.4.0\",\"0.2.0\",\"3.4.0\",\"0.6-1\",\"1.13.1\",\"0.6.12\",\"0.10\",\"1.1\",\"1.5-4\",\"1.4.3\",\"1.0.0\",\"3.4.0\",\"3.4.0\",\"3.4.0\",\"1.1-5\",\"0.3.6\",\"0.15.1\",\"1.16\",\"1.1.9\",\"0.20-35\",\"1.5\",\"1.1.0\",\"3.4.0\",\"0.12.11\",\"0.2.15\",\"1.5\",\"1.2\",\"0.4-3\",\"1.2-4\",\"1.2-0\",\"3.4.0\",\"1.1.5\",\"1.2.0\",\"3.4.0\",\"0.13\",\"0.4-4\",\"3.4.0\",\"1.0.2\",\"0.9-7\",\"2.1.14\",\"1.8-0\"],\"date\":[\"2017-01-18\",\"2017-04-21\",\"2017-04-21\",\"2017-05-30\",\"2017-04-21\",\"2017-04-01\",\"2017-05-13\",\"2017-01-27\",\"2016-10-11\",\"2013-07-31\",\"2016-12-29\",\"2016-07-10\",\"2010-04-06\",\"2017-04-21\",\"2017-04-21\",\"2017-04-21\",\"2017-03-12\",\"2017-04-28\",\"2015-08-27\",\"2017-05-18\",\"2016-07-10\",\"2017-03-25\",\"2014-11-22\",\"2017-04-21\",\"2017-04-21\",\"2017-05-22\",\"2014-11-03\",\"2017-04-26\",\"2017-01-16\",\"2017-05-15\",\"2016-12-22\",\"2016-09-03\",\"2017-04-21\",\"2017-04-07\",\"2017-02-18\",\"2017-04-21\",\"2016-11-17\",\"2017-04-20\",\"2017-04-21\",\"2016-06-20\",\"2014-01-02\",\"2016-11-12\",\"2017-04-12\"],\"source\":[\"CRAN (R 3.4.0)\",\"local\",\"local\",\"local\",\"local\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"local\",\"local\",\"local\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"cran (@1.16)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.3.3)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"local\",\"cran (@0.12.11)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"local\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"local\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"local\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\",\"CRAN (R 3.4.0)\"]}}"
    CMD ["R"]

## 5. Further customization

The `dockerfile()` function allows further customization regarding the R
version or the used base image (cf. Rocker stack). Note that while
choosing an R version for the Dockerfile explicitly is possible, the
session to generate the required information (i.e. which packages are
attached etc.) is still running the R version of the generating machine.

The following examples show usage of these options and the respective
`FROM` statements in the Dockerfile.

    df_custom <- dockerfile(from = NULL, r_version = "3.1.0", silent = TRUE)
    print(df_custom@image)

    FROM rocker/r-ver:3.1.0

    df_custom <- dockerfile(from = NULL, image = "rocker/geospatial", silent = TRUE)
    print(df_custom@image)

    FROM rocker/geospatial

    df_custom <- dockerfile(from = NULL, image = "rocker/verse:3.0.0", silent = TRUE)@image
    print(df_custom@image)

    [1] "rocker/verse"

## 6. CLI

A command line interface to the package functions is also available for
Linux based on [docopt.R](https://github.com/docopt/docopt.R). This
allows integration into workflows and tools written in other programming
languages than R.

You can make the command `containerit` available on your maching by
linking the R script file delivered with the package as follows:

`ln -s $(Rscript -e "cat(system.file(\"cli/container_it.R\", package=\"containerit\"))") /usr/local/bin/containerit`

CLI Examples:

      containerit --help
      
      # runs the first R markdown or R script file locally 
      # prints Dockerfile without writing a file
      containerit dir -p --no-write  
      
      # Packages R-script 
      # saves a workspace image (-i parameter)
      # Writes Dockerfile (overwrite with -f)
      # execute the script on start-up
      containerit file -ifp --cmd-R-file path/example.R

      # Creates an empty R session with the given R commands
      # Set R version of the container to 3.3.0
      containerit session -p -e "library(sp)" -e "demo(meuse, ask=FALSE)" --r_version 3.3.0

## 7. Challenges

We encountered several challenges during `containerit`'s development.
First and foremost, a well known limitation is that R packages don't
define system dependencies and do not provide explicit versions for R
package dependencies. The `sysreqs` package is a promising approach
towards handling system requirements, but so far lists package names but
does not provide version information. The
[shinyapps-package-dependencies](https://github.com/rstudio/shinyapps-package-dependencies)
demonstrate a (currently system dependent) alternative. The high value
of R might well lie in the fact that "packages currently on CRAN" should
work well with each other.

An unmet challenge so far is the installation of specific versions of
external libraries (see
[issue](https://github.com/o2r-project/containerit/issues/46)). A
package like `sf` relies on well-tested and powerful system libraries,
see `sf::sf_extSoftVersion()`, which ideally should be matched in the
created container.

And of course users may do things that `containerit` cannot capture from
the session state "after the analysis is completed", such as detaching
packages or removing relevant files, and unknown side-effects might
occur.

All software is presumed to be installed and run on the host system.
Although it is possible to use deviating versions of R or even create
Dockerfiles using sessionInfo-objects created on a different host, this
may lead to unexpected errors because the setup cannot be tested
locally.

## 8. Conclusions and future work

`containerit` alows to create and costumize Dockerfiles with minimal
effort, which are suitable for packaging R analyses in the persistant
runtime environment of a software container. So far, we were able to
reproduce complete R sessions regarding loaded and attached packages and
mitigate some challenges towards reproducible computational research.

Although we are able to package different versions of R, we still do not
fully support the installation of specific versions of R packages and
external software libraries, which R itself does not support. This
should be tested in the future by evaluating version-stable package
repositories like MRAN and GRAN or utility packages such as packrat --
see the [GitHub
issues](https://github.com/o2r-project/containerit/issues/new) for the
status of these plans or provide your own ideas there.

Related to installing specific versions is support for other package
repositories, such as Bioconductor, git, BitBucket, or even local files.
For now, it is recommended that users have all software up-to-date when
building a software container, as the latest version are installed from
CRAN during the image build, to have matching package versions between
the creation runtime environment and the container. All Dockerfiles and
instructions are adjusted to the Rocker image stack and assume a
Debian/Linux operating system. As we are not yet supporting the build of
Docker images from scratch, we are restricted to this setup.

The package is a first prototype available via GitHub. While a
publication on CRAN is a goal, it should be preceded by feedback from
the user community and ideally be accompanied by related packages, such
as [harbor](https://github.com/wch/harbor/issues/5), being available on
CRAN, too. The prototype of `containerit` was developed and tested only
on Ubuntu/Linux, which should be extended before releasing a stable
version on CRAN.

As part of the o2r project, it is planned to integrate `containerit` in
a [web service](http://o2r.info/architecture) for creating archivable
research in form of [Executable Research Compendia
(ERC)](https://doi.org/10.1045/january2017-nuest). Making `containerit`
itself easier to use for end-users is a secondary but worthwhile goal, for example by
building a graphical user interface for metadata creation. Country
locales are also not supported yet. We may want to support other
container OS (e.g. windows container or other Linux distributions) or
even containerization solutions such as
[Singularity](http://singularity.lbl.gov/) or the [Open Container
Initiative](https://www.opencontainers.org/)'s (OCI) [Image
Format](https://github.com/opencontainers/image-spec).

Feedback and contributions are highly welcome [on
GitHub](https://github.com/o2r-project/containerit/issues) or
[o2r\_project](https://twitter.com/o2r_project) on Twitter.

## Metadata

    sessionInfo()

    ## R version 3.4.0 (2017-04-21)
    ## Platform: x86_64-pc-linux-gnu (64-bit)
    ## Running under: Ubuntu 16.04.2 LTS
    ## 
    ## Matrix products: default
    ## BLAS: /usr/lib/libblas/libblas.so.3.6.0
    ## LAPACK: /usr/lib/lapack/liblapack.so.3.6.0
    ## 
    ## locale:
    ##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
    ##  [3] LC_TIME=en_GB.UTF-8        LC_COLLATE=en_US.UTF-8    
    ##  [5] LC_MONETARY=en_GB.UTF-8    LC_MESSAGES=en_US.UTF-8   
    ##  [7] LC_PAPER=en_GB.UTF-8       LC_NAME=C                 
    ##  [9] LC_ADDRESS=C               LC_TELEPHONE=C            
    ## [11] LC_MEASUREMENT=en_GB.UTF-8 LC_IDENTIFICATION=C       
    ## 
    ## attached base packages:
    ## [1] stats     graphics  grDevices utils     datasets  methods   base     
    ## 
    ## other attached packages:
    ## [1] fortunes_1.5-4    sp_1.2-4          gstat_1.1-5       containerit_0.2.0
    ## [5] knitr_1.16       
    ## 
    ## loaded via a namespace (and not attached):
    ##  [1] Rcpp_0.12.11         rstudioapi_0.6       magrittr_1.5        
    ##  [4] devtools_1.13.1      units_0.4-4          lattice_0.20-35     
    ##  [7] rjson_0.2.15         FNN_1.1              udunits2_0.13       
    ## [10] stringr_1.2.0        tools_3.4.0          xts_0.9-7           
    ## [13] grid_3.4.0           DBI_0.6-1            withr_1.0.2         
    ## [16] lambda.r_1.1.9       futile.logger_1.4.3  htmltools_0.3.6     
    ## [19] intervals_0.15.1     yaml_2.1.14          rprojroot_1.2       
    ## [22] digest_0.6.12        sf_0.4-3             futile.options_1.0.0
    ## [25] memoise_1.1.0        evaluate_0.10        rmarkdown_1.5       
    ## [28] stringi_1.1.5        compiler_3.4.0       backports_1.0.5     
    ## [31] spacetime_1.2-0      zoo_1.8-0
