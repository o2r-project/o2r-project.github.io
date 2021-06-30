---
layout: post
title: "geoextent presented at the 2021 Earth Cube"
author: "Sebastian Garzón"
categories:
  - geoextent
  - geospatial 
  - metadata 
  - scholarly publishing 
  - reproducibility
---

The Python library [geoextent](https://o2r.info/geoextent/) by the o2r project team was selected for presentation at the [2021 Earth Cube annual meeting](https://www.earthcube.org/2021-earthcube-annual-meeting) in the peer-reviewed notebooks session.
In this blog post, student assistant Sebastian reports from the event.

<!--more-->

## geoextent presented at the 2021 Earth Cube

Notebooks as a scholarly object, database interoperability, FAIR workflows, connecting data and code, and tools for geosciences research are some of the topics discussed at the [2021 EarthCube annual meeting](https://www.earthcube.org/2021-earthcube-annual-meeting).
At the event, o2r team members [Sebastian](https://orcid.org/0000-0002-8335-9312) and [Daniel](https://orcid.org/0000-0002-0024-5046) presented [geoextent](https://github.com/o2r-project/geoextent), a Python library designed to extract temporal and spatial extent from data files.

We presented the librry as part of the [2nd call for Notebooks](https://www.earthcube.org/2021-earthcube-annual-meeting) for a digital proceedings of the EarthCube Annual Meeting following the increased interest of the geosciences research community on reproducible workflows. 

# Exploring Research Data Repositories with geoextent.

> Sebastian Garzón and Nüst, Daniel. 2021. **Exploring Research Data Repositories with geoextent**. EarthCube Annual Meeting. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/earthcube2021/ec21_garzon_etal/HEAD)

The [notebook](https://mybinder.org/v2/gh/earthcube2021/ec21_garzon_etal/HEAD), accessible through [Binder](https://mybinder.org/), includes an introduction of geoextent's usage and a case study where we explored more than 300 [Zenodo](https://zenodo.org) repositories (over 25.000 files!) with geoextent.
An initial exploration of Zenodo's API showed that spatial metadata is rarely available, difficulting data integration and discovery.
The objective of our case study was to verify if we can increase the current percentage of repositories with geospatial information on [Zenodo](https://zenodo.org) by using geoextent.

[![](../public/images/2021-06-30-geoextent-presented-at-the-2021-Earth-Cube-meeting/Screenshot-presentation-zenodo-api.png)](../public/images/2021-06-30-geoextent-presented-at-the-2021-Earth-Cube-meeting/Screenshot-presentation-zenodo-api.png)  

*Screenshot of presentation showing the current state of spatial metadata in Zenodo*

Our results suggest that geoextent could be used to increase spatial metadata of repositories by directly extracting information from the files deposited on them. 
However, we identified a series of challenges for this approach including geospatial information being stored in ambiguous formats (e.g., CSV and `.asc` files) or incorrectly georeferenced files in specialized formats (e.g., missing coordinate reference system or flipped coordinates).
This case study also provide information for further development of geoextent to support more file formats and fix. 

[![](../public/images/2021-06-30-geoextent-presented-at-the-2021-Earth-Cube-meeting/Screenshot-presentation-results.png)](../public/images/2021-06-30-geoextent-presented-at-the-2021-Earth-Cube-meeting/Screenshot-presentation-results.png)

*Screenshot of presentation showing the results of our case study with geoextent*

For more information about geoextent you can follow these links:

- [geoextent repository](https://github.com/o2r-project/geoextent)
- [Exploring Research Data Repositories with geoextent - Binder](https://mybinder.org/v2/gh/earthcube2021/ec21_garzon_etal/HEAD)
- [Exploring Research Data Repositories with geoextent - presentation](doi.org/10.6084/m9.figshare.14786199)

## Earth cube meeting 2021

In addition to presenting geoextent, the participation in the event allowed us to get an insight into notebooks as research objects and scientific publications.
Some of the reflections on the evolution of the guidelines, review process, and selected notebooks with respect to the first call were discussed in a [panel](https://www.youtube.com/watch?v=IV-4e3kxVas).
In the same panel, representatives of the Jupyter, R&nbsp;Markdown, and Matlab communities presented different tools to share research results and how they could be integrated better within the context of scientific publications.

Among the other [18 accepted notebooks](https://docs.google.com/document/d/1gkIGbqUtiy6AQ-OsnHq6xni2sA_8Hhn80VASPKW4uD8) we found interesting tools, for example *cf_xarray*, used to simplify the usage of Climate and Forecast (CF) compliant datasets by improving the metadata of files [![Binder](https://mybinder.org/badge_logo.svg)](https://binder.pangeo.io/v2/gh/earthcube2021/ec21_cherian_etal/main?filepath=DC_01_cf-xarray.ipynb), a methodology to access to OpenTopography’s Cloud Optimized GeoTIFF data for topography information [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/earthcube2021/ec21_beckley_etal/HEAD)or tools to teach kids about glaciers [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/OGGM/binder/EarthCube21).
All of these studies give us a picture of different geosciences research questions and how they are presented in fully reproducible environments.
