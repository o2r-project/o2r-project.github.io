---
layout: post
title: 'Opening Reproducible Research with OJS'
categories:
  - OJS
  - eLife
  - 'Open Science'
  - community
  - Binder
author: 'Daniel Nüst, Tom Niers'
---

Data and software are crucial components of research.
They go well beyond the workflows one would call _Data Science_ today. Only openly available building blocks can ensure transparency, reproducibility, and reusability of computer-based research outputs.
More and more researchers rely on small or large datasets and use analysis tools to analyse variables, create figures, and derive conclusions.
That is why the project Opening Reproducible Research ([_o2r_](https://o2r.info/)) implements the concept of the Executable Research Compendium ([ERC](https://o2r.info/erc-spec/)) to capture all bits and pieces underlying a research article.
In a [pilot study](/pilots), we plan to connect the Open Journal Systems ([OJS](https://pkp.sfu.ca/ojs/)) with the ERC.
On the one hand this connection enables submission, review, and publishing of [research compendia](http://research-compendium.science/) and ERC.
On the other hand while it leverages the publishing capabilities and workflow management of OJS.
We will implement this integration in form of an [OJS plug-in](https://docs.pkp.sfu.ca/learning-ojs/en/settings-website#plugins) so it becomes readily available for all maintainers of OJS instances.

In this blog post [Tom](https://github.com/tnier01) and [Daniel](https://orcid.org/0000-0002-0024-5046) describe our general procedure, the first concrete plug-in idea, and the planned plug-in structure.

_o2r_ is a joint project by the Institute for Geoinformatics ([ifgi](https://www.uni-muenster.de/Geoinformatics/en/)) and the University and State Library ([ULB](https://www.ulb.uni-muenster.de/)) at the University of Münster ([WWU](https://www.uni-muenster.de/)).
The project is supported by the German Research Foundation ([DFG](https://www.dfg.de/), see [About](/about) page for details).

## Procedure

After a first collection of ideas we started concretizing them in [user stories](https://en.wikipedia.org/wiki/User_story).
The main user stories concern the idea of making research compendia, such as ERC, useable in the OJS-workflow (see details in the next paragraph).
These stories may contain potentially generic features that could be realised as individual plug-ins for

- uploading multiple submission files, even from cloud storage, including large size files and public or authenticated shares, e.g. ownCloud, Dropbox, or GitHub,
- connecting articles with external data repositories (e.g. listing and preview of supplemental data published in [Open data repositories](https://en.wikipedia.org/wiki/Open-access_repository)),
- supporting [literate programming](https://en.wikipedia.org/wiki/Literate_programming)-based article formats (e.g. ERC with R Markdown, Jupyter Notebooks) with rendering to HTML and/or PDF, or
- seamlessly connecting articles with interactive online workspaces with reusable data and code as an alternative to static fixed articles (e.g. using [Binder](http://mybinder.org/)).

However, the focus will initially be on the integration of a full ERC-based workflow into OJS.
At a later stage, parts of this integration could be the starting point for the above individual plug-ins.

Based on the user stories, we then developed a few mockups (or [wireframes](https://en.wikipedia.org/wiki/Website_wireframe)) to get a better understanding how our ideas will likely look and to ease communication about the stories. 
The next step starts now: we develop the plug-in based on our mockups and user stories.
To make sure we're on the right track we want to use this blog post to connect with the OJS community on our ideas and specifically search for feedback on the plans described below. 

## User stories

The full list of user stories can be found [in this spreadsheet](https://uni-muenster.sciebo.de/apps/onlyoffice/1513199997?filePath=%2FNiers%2FuserStories2.0_blogArticle.xlsx).
They are roughly sorted by priority.
We even tried to guesstimate the efforts, though we expect to be quite far off during the first few stories until we get a better understanding of developing with OJS.

The following main user stories will be implemented first.
They can be grouped into stories concerning creation (inluding upload) and examination (viewing, manipulating) ERCs.

**ERC creation in OJS**

- As author I want to upload all my files (data, code, text) directly from my computer, so that I save time (not each file individually) and the complete workflow is published.
- As author I want to insert the metadata for a submission at one location, so that I do not have to insert them several times. 
- As editor I want my authors to be able to upload an (optional "executable") research compendium from their computer, so that data and software can be published as a unit and I can find suitable reviewers.
- As editor I want there to be a review step regarding reproducibility of the article, so that the quality of reproducibility of articles in my journal increases.
- As editor I want research compendia in general and ERCs to be automatically validated on the platform, so that I don't have trouble with them and the compendia are  nevertheless complete.
- As site admin I would like to install a Research Compendium Upload from my computer as a plug-in in OJS, so that I can offer this feature to authors.

**ERC examination in OJS**

- As reviewer I want to view, download, survey and manipulate the ERC, so that I can check even complex workflows without much additional effort. 
- As reader I want to view, download, survey and manipulate the ERC within the article page, so that I am able to understand the research work. 
- As editor I would like the readers of the journal to be able to view the ERC in the issue of the journal, so that the quality of the journal increases. 
- As site admin I want to be able to install a plug-in in OJS that allows you to view and manipulate ERCs, so that I can offer this feature to authors and reviewers.

## ERC plug-in for OJS

_How do we want to realize our user stories?_

### Upload Executable Research Compendium

To replace a regular article with an ERC in OJS, there is of course the need to upload it.
The idea is to add a new file type for finished ERCs.
But we also want to give the user the opportunity to create a ERC during the submission process within OJS.
Therefore we plan to customize the upload process.
The user will have the option to upload the files for the ERC and then to modify ERC metadata (publication metadata, spatio-temporal metadata).
The authors will also be able to create [bindings](/2019/08/28/bindings/).
The following mockup shows how we imagine the upload process of an ERC.

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup1.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup1.png)
Mockup 1.: Submit an ERC in OJS (metadata form)

### Review Executable Research Compendium

After uploading the article, the next step in the OJS workflow is the review prozess.
In this process the reviewer should be able to both download the ERC and to inspect the ERC online.
Therefore a preview is needed, which does not differ from the view the reader is finally seeing.
The preview only shows an additional link which brings the reviewer back to the review page.
In this view the user can read the main text document of the ERC (PDF or HTML), look at data and code files and figures, and manipulate a workflow with bindings.
To provide feedback to the author, a new text area "Reproducibility Review" is added to the third step "Download & Review" in the review stage in OJS. Here the reviewer can comment on the understandability and reproducibility of the given workflow.

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup2.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup2.png)
Mockup 2.: Examine an ERC subission (download, preview links) and write review comments (reproducibility text box)

### Examine Executable Research Compendium 

The examiniation of an ERC in OJS, i.e. the viewing of compendium files and manipulation of workflows by reviewers and readers, is a core feature of the plug-in.
The only differ in the link to get back to either the review form in the case of the reviewer or back to the article landing page in the case of the reader.
We have two two different ideas how to realize ERC examination.

First, there is the possiblity to integrate it directly on the main article page.
The ERC with its file view and manipulation area is directly shown on the article page.

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup3.1.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup3.1.png)
Mockup 3.1: View of an ERC for a reader (idea 1)

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup3.2.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup3.2.png)
Mockup 3.2: View of an ERC for a reviewer (idea 1)

Second, a realization similar to [lensGalleyBits](https://github.com/paflov/lensGalleyBits) is imaginable.
In this case the reader is taken to a new page where can can show the regular o2r platform's user interface.

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup4.1.1.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup4.1.1.png)
Mockup 4.1.1: View of an ERC for a reader - article view (idea 2)

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup4.1.2.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup4.1.2.png)
Mockup 4.1.2: View of an ERC for a reader - ERC view (idea 2)

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup4.2.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/Mockup4.2.png)
Mockup 4.2: View of an ERC for a reader (idea 2)

In both cases the user has all possibilitys concerning reading the PDF of the ERC and manipulating its figures and tables.
In the first case we preserve the journal's branding at the top of the page, which might be desirable for editors and publishers.
In the second case we only have the default o2r UI which might be easier to integrate as a standalone page.

## Plug-in structure

We sketched a structure for our ERC plug-in.
The plug-in consists of two parts, one for the examination of ERCs and one part for the creation/upload of ERCs.
The [plug-in category](https://docs.pkp.sfu.ca/dev/plugin-guide/en/categories) or type probably needs to be a "generic" plug-in to realise the deep integration of ERC into many different pages of OJS.

[![](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/o2r2_OJS_plug-in.png)](/public/images/2019-10-15-Opening-Reproducible-Research-with-OJS/o2r2_OJS_plug-in.png)
Plug-in structure of (E)RC in OJS  

## Conclusion

We hope this post gives you a good impression of our plans.
As you may have noticed, some of the features we plan to implement for ERCs might also be interesting for OJS users who just want to upload multiple files, for journals who want to support other types of [research compendia](https://research-compendium.science/), or for an OJS maintainer who wants to allow a Markdown based workflow.
We can imagine several plug-ins could be extracted from the ERC plugin [as described above](#procedure), depending on time left in our schedule and interest by other OJS users/developers.
_What do you think?_

Please do not hesitate to comment on this blogpost with your ideas and questions.
We would be pleased about any feedback. 


