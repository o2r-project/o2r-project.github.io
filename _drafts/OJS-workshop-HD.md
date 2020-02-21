---
layout: post
title: Next generation journal publishing and containers
author: "Daniel Nüst"
layout: post
categories:
  - Heidelberg
  - OJS
  - workshop
---

Some challenges of working on the next generation of research infrastructures can be solved most effectively by talking to other people.
That is why o2r team members Tom and Daniel were happy to learn about the [announcement](https://www.ojs-de.net/news-und-veranstaltungen/news/save-the-date-ojs-entwickler-workshop-am-20-21022020-in-heidelberg) of an [Open Journal Systems](https://pkp.sfu.ca/ojs/) (OJS) [workshop organised by Heidelberg University Publising (heiUP)](https://journals.ub.uni-heidelberg.de/index.php/ojs/announcement/view/103).

The o2r team was a little bit the odd one out.
Other workshop participants<!--more--> either had extensive OJS development experience, or were not developers at all but running production systems of many OJS journals across the German university landscape.
But that could not keep us from from telling everyone about [Executable Research Compendia](https://doi.org/10.1045/january2017-nuest), of course.
We briefly summarised our plans to [extend OJS with ERC capabilities](/2019/10/15/Opening-Reproducible-Research-with-OJS), _but we also had new stuff to share!_
Tom is considering to put his _geo_-informatics skills to use and extend the metadata of OJS articles with geospatial features in his Bachelor thesis.
This would allow to display the spatial area of articles on a map, and even browse articles by their location(s).
Learn more about these ideas in our [slides](https://docs.google.com/presentation/d/1TilFah9E6wOdtTZYlNf5BjfSGCzhKQCooa-6wSBisG0/).

<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Today team members <a href="https://twitter.com/nordholmen?ref_src=twsrc%5Etfw">@nordholmen</a> <a href="https://twitter.com/herrniers?ref_src=twsrc%5Etfw">@herrniers</a> meet the German <a href="https://twitter.com/hashtag/OJS?src=hash&amp;ref_src=twsrc%5Etfw">#OJS</a> developer and user community at a workshop organised by <a href="https://twitter.com/heiUP_HD?ref_src=twsrc%5Etfw">@heiUP_HD</a> <a href="https://twitter.com/ojs_pkp?ref_src=twsrc%5Etfw">@ojs_pkp</a> <br><br>Of course we want to talk <a href="https://twitter.com/hashtag/spatial?src=hash&amp;ref_src=twsrc%5Etfw">#spatial</a> data and <a href="https://twitter.com/hashtag/ERC?src=hash&amp;ref_src=twsrc%5Etfw">#ERC</a> in OJS!<br><br>🌍❤️📚<a href="https://twitter.com/hashtag/SpatialIsSpecial?src=hash&amp;ref_src=twsrc%5Etfw">#SpatialIsSpecial</a> <a href="https://twitter.com/hashtag/ResearchCompendium?src=hash&amp;ref_src=twsrc%5Etfw">#ResearchCompendium</a> <a href="https://twitter.com/hashtag/ScholComm?src=hash&amp;ref_src=twsrc%5Etfw">#ScholComm</a><a href="https://t.co/5FenW7WUae">https://t.co/5FenW7WUae</a> <a href="https://t.co/BrxkAiSE72">pic.twitter.com/BrxkAiSE72</a></p>&mdash; o2r (@o2r_project) <a href="https://twitter.com/o2r_project/status/1230482699930013697?ref_src=twsrc%5Etfw">February 20, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

But Tom and Daniel also came with a mission: to jumpstart the struggling OJS developments with the help of some experiences OJS developers.
None of our team has extensive experience with PHP, so getting control over the huge OJS codebase and setting up a proper development environment _with debugging_ was an important task they've been pushing aside since autumn last year.
_And we got it!_ 
[Note to self: don't forget to enable `remote_enable` and `remote_autostart` for Xdebug in the file `/etc/php/7.3/cli/conf.d/20-xdebug.ini` for debugging to work - then the default VSCode configuration with port `9000` will just work (-:].
On top of that, Tom got a very helpful introduction to writing OJS plug-ins, and Daniel now has a good graps on the [currently developed Docker images for OJS](https://github.com/pkp/docker-ojs/).
The Docker images are not a simple project, since the PKP teams plans to support multiple webserver implementations, multiple PHP versions, and all OJS versions still in production somewhere... phew!
Daniel even [opened a pull request](https://github.com/pkp/docker-ojs/pull/14) and suggests a different way to support both remotely and locally built images.
This prepares us well for the moment when we want to run OJS on our own servers - in containers of course.

So the expectations were high, but not eventually they were not disappointed.
Daniel was glad to see some familiar faces from the [OJS-de.net community](https://www.ojs-de.net/) he met at a previous workshop in Heidelberg.
The new contacts made were more just as important as the helpful push towards becoming real "OJS devs" 🐱‍💻.
Other groups at the workshop reported very interesting results, for example on the connection of OJS with proper digitial archives (with promising mentions of also archiving data... and code?), more flexible publishing workflows with own tools (mentioning Pandoc, which might make these flexible pipelines a first  step towards (R) Markdown-based OJS publications ⚙️), and using search indexes such as Solr and Elasticsearch within OJS (which also have geospatial capabilities 💯).
As you can see, we're very hopeful future collaborations will spark from these educational and entertaining encounters.
