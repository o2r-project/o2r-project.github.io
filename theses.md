---
layout: page
title: 📖 Theses
categories:
  - o2r
  - o2r2
  - theses
  - thesis
  - student research
  - students
  - BSc
  - MSc
  - GeoTech
exclude_from_all_pages: true
---

<script type="text/javascript" src="{{ '/public/js/jquery.js' | absolute_url }}"></script>

The following **o2r thesis topics** are open, under development, or have been supervised in the context of o2r.
Please contact `o2r.team@uni-muenster.de` if you are a student (ifgi BSc, ifgi MSc, MSc GeoTech, computer science @ WWU, ...) interested in one of the open topics or in helping to solve other important challenges of scholarly publishing and scholarly communication.

## Completed

- Suleiman, J., **A parameter-based model for map comparison and conversion** (BSc, April 17, 2017)
  <br />Supervisors: M.Sc. Markus Konkol, Dr. Max Florian Pfeiffer
  <br /><span class="expandable"><a href="#">Abstract ↓</a></span>
  <blockquote class="abstract">
    <p><em>The comparison of thematic maps is a common task in Geosciences which can be demanding depending on the map visualizations’ level of comparability. However, through reproducible research the underlying data for creating maps in scientific publications is accessible and therefore visualizations can be changed. By providing combinations of visualizations that facilitate thematic map comparison, scientists are able to compare maps more effectively. The aim of this thesis is to examine and establish parameters that enhance thematic map comparability. By integrating these parameters into a parameter-set that enables thematic map conversions, comparisons can be facilitated. To achieve this, a study was conducted to derive guidelines for enhancing the comparability of choropleth and proportional symbol maps and the parameter-set was developed. Necessary metadata can be collected through automated metadata extraction, which avoids additional efforts for both author and user. A prototype was implemented that includes all these features and was integrated into the o2r project.</em></p>
  </blockquote>
- Mohr, M., **Machine-based extraction of location information from digital publications** (MSc, December 12th, 2017)
  <br />Supervisors: Prof. Dr. Christian Kray, M.Sc. Markus Konkol
  <br /><span class="expandable"><a href="#">Abstract ↓</a></span>
  <blockquote class="abstract">
    <p><em>“Which publications covering land use in Brazil are available?” is an example for a question one could ask a search engine for scientific publications. Expressing this with an appropriate search term would only find a subset of the potential results. This is due to the text based search index, which can only find the papers that include the country name “Brazil”, but no papers that mention a local name like “Rio de Janeiro” in the text. A number of excellent search engines exist for scientific publications, but they are mainly focused on text-based content. As a consequence, searching for content with a spatial relation is a sophisticated task. In this thesis, an automatic approach to extract location information from digital scientific publications is developed. It allows parsing spatial information from figures and texts. Geographical names and coordinates can be automatically extracted from texts. Additionally, maps can be detected from the figures contained in publications. These maps can then be analyzed using three approaches with regards to the spatial information they provide: (1) World maps can be recognized and (2) the spatial extent of maps can be parsed from coordinates and their corresponding axes. (3) Lastly, of course, geographical names offer important information. All methods are embedded in a framework designed to support further development. The key challenge is to analyze the textual and graphical content and combine the information retrieved from these sources to a single spatial reference. This challenge is addressed by combining existing tools for subtasks such as named entity recognition and image classification and newly developed methods to an extensive library for spatial analysis tasks. The proposed solution is thoroughly evaluated on a real-word annotated data set.</em></p>
  </blockquote>
- Lohoff, L., **Similarity Measurements for Executable Research Compendia** (MSc, January 30, 2018)
  <br />Supervisors: Prof. Edzer Pebesma, Daniel Nüst
  <br /><span class="expandable"><a href="#">Abstract ↓</a></span>
  <blockquote class="abstract">
    <p><em>Recommender systems are a feature often used to present related items to users in different areas such as shopping, job networks or research websites. They incentivize the user to explore the available set of items in the system. Ideally the user gets a better picture of the available items and it helps them find what they searched for. With the rise of computational research, publications become more sophisticated and complicated. They have to deal with multiple software components in the creation process to analyze the data and create visualizations. However, research also is becoming increasingly computational and controlled, offering potential for analysis and collaboration. This change allows to analyze computational research publications for more than just the document text: The source code, the dataset and metadata can contain important information helping to determine similar papers. These could form sections such as spatially similar or computationally similar suggestions. This thesis explores the methods of analyzing supplementary information for similarities to find related publications. The focus is set on (1) spatial files which are often part of research papers in the geosciences and on (2) source code used to process the data. Two methods for spatial and source code analysis are implemented in a prototype: A geohash based spatial index similarity and a information retrieval (IR) method to analyze the source code. Both methods rely on the search database Elasticsearch. To evaluate this type of similarity, the prototype is used to analyze the similarity of a test dataset containing research papers with supplementary information.</em></p>
  </blockquote>
- Sunni, I., **Testing Geospatial R Packages on Implementations of the R language and Platforms** (MSc GeoTech, January 2020)
  <br />Supervisors: Prof. Edzer Pebesma (ifgi), Daniel Nüst (ifgi), Roberto André Pereira Henriques (Universidade NOVA de Lisboa)
  <br />Full text online: [http://hdl.handle.net/10362/95140](http://hdl.handle.net/10362/95140)
  <br /><span class="expandable"><a href="#">Abstract ↓</a></span>
  <blockquote class="abstract">
    <p><em>R is a programming language for statistical computation and graphics. Besides the commonly used, GNU R, there are other alternative R implementations that claim to have advantages compared to the GNU R. Unfortunately, it is not clear how will geospatial R packages behave on these implementations since these packages often rely on system libraries which installed at the system level. System libraries also depend on the platform where the R is running. To find this information, this research aims to explore the compatibility of geospatial R packages on different R implementation and platform. This research also aims to see which R implementation and platform has the best performance. To make the exploration easier, container technology is used to install system dependencies and R implementations. All system dependencies from sysreqsdb are installed for geospatial R packages. From this exploration, it is found that not all R implementations are compatible with geospatial packages. Problems found can be grouped into three categories: System Dependencies, Unsupported Implementation, and Running Time Error. GNU R and Microsoft R Open (MRO) are the only R implementations that compatibles with geospatial R packages. A benchmarking R package called altRnative is created to run the benchmarking across the successful combination. The benchmark result shows that GNU R has a little bit better performance (1.2x) compared to MRO regardless of the platforms. Reproducibility self-assessment (https://osf.io/j97zp/): 3, 3, 3, 3, 3 (input data, preprocessing, methods, computational environment, results).</em></p>
  </blockquote>

## In progress

- Niers, T. **"GeoOJS"** (BSc.)
  <br />Supervisors: Daniel Nüst, NN

## Open

- See the catch-all topic **"Opening Reproducible Research (o2r)"** on [public listing of thesis topics at ifgi](https://www.uni-muenster.de/Geoinformatics/en/Studies/thesis/index.php)) for thesis topics on interacting with scientific data and publications and user studies.
- **Trusted data repositories for executable research compendia**
  <br />Contact: Daniel Nüst
  > _Computational research introduces challenges when it comes to reproducibility, i.e. re-doing an analysis with the same data and code. A current research project at ifgi developed a new approach called Executable Research Compendia (ERC, see https://doi.org/10.1045/january2017-nuest) to solve some of these challenges. ERC contain everything needed to run an analysis: data, code, and runtime environment. So they can be executed “offline” in a sandbox environment. An open challenge is the one of big datasets and reducing data duplication. While the idea of putting “everything” into the ERC is useful in many cases, once the dataset becomes very large it is not feasible to replicate it completely for the sake of reproducibility/transparency and to some extent for archival._
  > _This thesis will create a concept for allowing ERC to communicate with specific data repositories (e.g. PANGAEA, GFZ Data Services) extending on previous work (https://doi.org/10.5281/zenodo.1478542). The new approach should let ERCs “break out” of their sandbox environments in a controlled and transparent fashion, while at the same time more explicitly configuring the allowed actions by a container (e.g. using AppArmor)._
  > _Since trust is highly important in research applications, the communication with remote services must be exposed to users in a useful and understandable fashion. Users who evaluate other scientists ERC must know which third party repositories are used and how. The concept must be (i) implemented in a prototype using Docker containerization technology and discussed from viewpoints of security, scalability, and transparency, and (ii) demonstrated with ERC based on different geoscience data repositories, e.g. Sentinel Hub, and processing infrastructure, e.g. openEO or WPS, including an approach for authentication. Furthermore it could be evaluated to define the sandbox more explicitly, and if the communication between ERC and remote service can be captured and then cached for an additional backup, so that future execution may re-use that backup._
  > 
  > _Prior experience with Docker is useful but not a strict requirement._
- **Executable Research Compendia for Python and Open GIS**
  <br />Contact: Daniel Nüst
  > _The Executable Research Compenium (ERC) developed by Opening Reproducible Research (https://o2r.info) provides an approach for solving the challenges of reproducibility and reusability of scholarly research in the geosciences. With the help of a UI and a reproducibility service, academic authors can easily create a snapshot of their research workflow at the time of submitting it for a peer review. However, the ERC is currently limited to workflows based on R and using R Markdown. In this work, the student will explore what changes need to be made to the ERC specification to support geospatial workflows in Python. How can users of common open source GIS (e.g. QGIS) be supported in packaging their scripted workflow in an ERC, ideally without any programming? How can suitable virtual environments (i.e. Dockerfiles) be derived from the workspace metadata (e.g. QGIS project file) and workflow (e.g. created with QGIS Process Modeller)?_
  >
  > _The student should have an interest in working with an existing codebase and multiple programming languages. Some experience with Node.js, Python, and Docker is useful._
- **Geoservice ERC**
  <br />Contact: Daniel Nüst
  > _Geospatial research workflows today are completely digitised. More and more observational data is available in open repositories and analysed with open software. The processing is increasingly moved to scalable cloud infrastructures, which often build on free and open source software. A downside is that the digitisation, data volume, online processing, and complexity of software environments make it harder for researchers to understand, reproduce, and build upon each others work. The executable research compendium (ERC) developed by the project Opening Reproducible Research (o2r, https://o2r.info) attempts to lower the barriers for inspecting and manipulating published research workflows in the geosciences. In this thesis, the student will explore how common geospatial web services can be packaged as part of a research compendium. These web services should comprise data services (e.g. a WFS, SOS, WCS), view services (e.g. a WMS) and  processing services (e.g WPS, openEO). The student will re-use published or develop two to three example workflows using based on these web services. The ERC and supporting tools currently only support a single Docker container for capturing the runtime environment. A core challenge of this work will be to find out how multiple containers may be created and executed without additional burden on the author of a research paper during the creation of ERC, and without introducing security risks in the networking between the containers._
  > 
  > _Affinity to command line tools and solving hard problems using existing software tools is a prerequisite for this thesis. The student will get to know a variety of common geospatial web services (e.g. Geoserver, SciDB, 52N WPS, pyWPS) and Docker during the course of this work._
- **Open Reproducible Notebooks for GIS**
  <br />Contact: Daniel Nüst, Markus Konkol
  > Open Science, particularly reproducible research, is crucial to increase the impact of science in society, as well as to accelerate scientific discovery. A useful tool for more effective and sustainable communication of research workflows are digital notebooks. Based on the literate programming paradigm, they integrate text and code in a coherent manner. However, a notebook approach is more easily connected with script base GIS workflows, e.g. using R, but has not yet been connected with popular GIS featuring a graphical user interface (GUI), such as ILWIS (Integrated Land and Water Information System, https://52north.org/software/software-projects/ilwis/) or QGIS (https://qgis.org/). In GUI-based GIS it is difficult for scientists to fully describe the steps that were carried out to achieve the reported reported results in a regular scientific article.
  > 
  > Therefore this thesis investigates how to facilitate packaing and sharing workflows created in a GUI-based GIS based on common notebook technologies, such as Jupyter (https://jupyter.org/) or R Markdown (https://rmarkdown.rstudio.com/). The student makes the GIS kernels accessible in the code cells of these notebooks comparing different approaches, e.g., the ILWIS Python API vs. ILWIS scripting language. Furthermore a seamless transfer of workflows created in the GUI into notebooks will be designed and evaluated, e.g. in the form of a Jupyter extenion, a QGIS plug-in, or an RStudio Add-in. Two reproducible worklows illustrate the implemented approach.
  > 
  > The student should have experience in working with existing codebases of open source software and be open to complex programming challenges. An affinity to working with multiple programming languages and prior experience with Python, R, and optionally C++ are benefitial.

<script>
$('.expandable').click(function(){
  $(this).next().slideToggle('slow');
});
</script>