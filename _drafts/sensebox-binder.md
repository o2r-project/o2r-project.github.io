---
layout: post
title: Open environmental data analysis
categories:
  - senseBox
  - openSenseMap
  - 'open science'
  - 'open data'
  - 'open source'
  - 'environmental data'
author: 'Daniel Nüst'
---

_This article is cross-posted in German on the [senseBox blog](https://sensebox.de/de/blog)._

It's the time of the year to make resolutions and to see beyond one's own nose.
For o2r team member Daniel, this meant to explore what he could do with his brand new _[senseBox:home](https://sensebox.de/de/products)_ and the awesome _[BinderHub](https://binderhub.readthedocs.io)_ instead of putting it on the back burner.

[![screencast of senseBox-Binder analysis in RStudio running on mybinder.org](https://media.giphy.com/media/l49JRjO65S0WQ1Kyk/giphy.gif)](https://media.giphy.com/media/l49JRjO65S0WQ1Kyk/giphy.gif)

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/v2/gh/nuest/sensebox-binder/master)

Building on a deep stack of Open Hardware, Free and Open Source Software, and Open Data, he created <!--more-->a fully open analysis of particulate measurements at New Year's Eve in Münster.
With just a few clicks you can open the exact computational environment which he utilized to retrieve historic sensor data from the openSenseMap API, and to analyse and visualise it with R.
And all that without installing any software to your computer, all you need is a web browser.

The following screenshots show the RStudio and Jupyter Notebook renderings of the workflow.

[![screenshot of senseBox-Binder analysis in RStudio](/public/images/2018-01_sensebox-binder-rstudio-screenshot.png)](/public/images/2018-01_sensebox-binder-rstudio-screenshot.png)

[![screenshot of senseBox-Binder analysis in Jupyter Notebook](/public/images/2018-01_sensebox-binder-jupyter-screenshot.png)](/public/images/2018-01_sensebox-binder-jupyter-screenshot.png)

And of course he worried about reproducibility and put in several layers of backup! Learn all about it at the GitHub repository:

**[https://github.com/nuest/sensebox-binder/](https://github.com/nuest/sensebox-binder/)**

Or get a peak at the output of the analysis here: [https://nuest.github.io/sensebox-binder/sensebox-analysis.html](https://nuest.github.io/sensebox-binder/sensebox-analysis.html)

And we were not the only ones taking a look at particulate matter in Germany using R.
[Johannes Friedrich](https://johannesfriedrich.github.io/), researcher at [University of Bayreuth](http://www.lumi.uni-bayreuth.de/), used his R package [senseBox](https://github.com/JohannesFriedrich/senseBox) to download and plot data of over 400 senseBoxes. See [his blog](https://johannesfriedrich.github.io/2018-01-11-particular-matter-new-year/) for his findings.