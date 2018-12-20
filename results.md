---
layout: page
title: Results
description: Project results
---

_Please find a project description and information about the team and partners on the [about page](/about), and a complete list of publications and presentations on the [publications page](/publications)_.

## Specifications & documentation

o2r is an open project, so all our components are openly developed [on GitHub]({{ site.github.org }}). The project's findings manifest themselves in the following core specifications and documents, all of which are under development.

- **[ERC specification](https://o2r.info/erc-spec)** ([source](https://github.com/o2r-project/erc-spec)) formally defines the Executable Research Compendium and provides some background.
- **[Architecture](https://o2r.info/architecture/)** ([source](https://github.com/o2r-project/architecture)) describes multiple levels of architecture, from the relation of our reprocibility service with other platforms down to internal microservices.
- **[Web API](https://o2r.info/api/)** ([source](https://github.com/o2r-project/api)) defines a RESTful API for our reproducibility service, also used by our platform client.

To cite the specifications and documentations please use

> Nüst, Daniel, 2018. Reproducibility Service for Executable Research Compendia: Technical Specifications and Reference Implementation. Zenodo. doi:[10.5281/zenodo.2203844](http://doi.org/10.5281/zenodo.2203844)

## Implementation & demo

We develop a reference implementation of the mentioned specification as Open Source software on GitHub: **[{{ site.github.org }}]({{ site.github.org }})**

**Try the online demo at [https://o2r.uni-muenster.de](https://o2r.uni-muenster.de)** and if you are a developer find the web API endpoint at [<code>https://o2r.uni-muenster.de/api/v1/</code>](https://o2r.uni-muenster.de/api/v1/).

**Try it out on your own machine with the [reference-implementation](/2017/10/31/reference-implementation/)** (only Docker required!):

`git clone https://github.com/o2r-project/reference-implementation`
`docker-compose up`

Watch a short **video** of our platform prototype (turn on subtitles!):

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Vy9b3pIWPd0?rel=0" frameborder="0" allowfullscreen></iframe>

To cite the reference implementation please use

> Nüst, Daniel, 2018. Reproducibility Service for Executable Research Compendia: Technical Specifications and Reference Implementation. Zenodo. doi:[10.5281/zenodo.2203844](http://doi.org/10.5281/zenodo.2203844)