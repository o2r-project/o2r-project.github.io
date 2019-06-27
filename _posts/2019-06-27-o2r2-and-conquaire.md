---
layout: post
title: "o2r2 @ Conquaire Workshop"
categories:
  - "funding"
  - "DFG"
  - "project"
  - "EGU"
  - "pilots"
  - "Copernicus"
  - "press"
  - "poster"
  - "conquaire"
author: "Markus Konkol"
---

Now that we have two more years to work on open reproducible research (see our last [blog post](https://o2r.info/2019/04/15/o2r2-and-egu/)), there is also some space for an exchange with related projects and to explore potential new collaborations. We were thus very happy to receive an invitation from the [Conquaire](https://conquaire.uni-bielefeld.de/about/) project at the University of Bielefeld for the workshop on [data quality and reproducibility](https://uni-bielefeld.de/(en)/conquaire/reproducibility-workshop/) (03.04.2019). Conquaire started about the same time as o2r and strives for similar goals, i.e. assisting scholars in making their research results reproducible and reusable. The workshop was located at the Center for Interdisciplinary Research in a very nice room that looked a bit like the United Nations headquarter - so it was good practice for the bigger goals we have in mind. 
[![room](/public/images/o2rconquaire.jpg)](/public/images/o2rconquaire.jpg)

[Prof. Dr. Philipp Cimiano](http://www.sc.cit-ec.uni-bielefeld.de/de/team/philipp-cimiano/) gave the first talk of the day. He presented the general Conquaire approach which focuses on storing all materials in a GitLab repository and running checks with the help of continuous integration based on [Jenkins](https://jenkins.io/). Researchers can thus create an incremental publication where each  git commit triggers and automatic validation process. They also had a promising number of use cases. However, similar to us, they struggled a bit with the amount of effort needed from authors to make research reproducible.

[Christian Pietsch](https://www.ub.uni-bielefeld.de/~cpietsch/) then gave a quick introduction into versioning tools such as GitLab and which benefits users get. I particularly liked his answer to the question from the audience if the Conquaire approach is also feasible with licensed software: Use free open source software! It’s that easy.

Afterwards, Conquaire team member Fabian Herrman talked about their validation approach by using continuous integration ([Slides](https://www.ub.uni-bielefeld.de/div/kwi_vortraege/2019-04-12_UB-Kolloquium_Conquaire_qc_herrmann.pdf)). They check, for example, if all files are available (including readme and license) and convey the result in two ways: First, by assigning a badge to the repository and second, by emailing the author of the repository. 

The following talks were about **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable data principles (by Silvia Wissel and Amrapali Zaveri) and the Jupyter Notebook, which was used in the context of history science by Malte Vogl. One benefit of Jupyter notebooks he mentioned stuck with us: it is also readable when the base software does not exist anymore. This is also one of the essential advantages of the Dockerfiles and R Markdown documents used in our executable research compendia (ERCs). 

Last but not least, we were allowed to present our approach and what we plan to achieve in the next two years. The slides are available online: [https://zenodo.org/record/2628278](https://doi.org/10.5281/zenodo.2628278).