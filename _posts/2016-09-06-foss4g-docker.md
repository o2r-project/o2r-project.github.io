---
layout: post
title: Docker presentation at FOSS4G conference
categories:
  - Docker
  - FOSS4G
  - conference
  - presentation
  - video
---

**Update**: A video recoriding of the presentation is now published on the TIB AV-Portal: [http://dx.doi.org/10.5446/20330](http://dx.doi.org/10.5446/20330)

<iframe width="560" height="315" scrolling="no" src="//av.tib.eu/player/20330" frameborder="0" allowfullscreen></iframe>

o2r team member [Daniel Nüst](https://twitter.com/nordholmen) recently participated in the worlds largest conference for geospatial open source software. The [FOSS4G 2016](http://2016.foss4g.org) was hosted by the Open Source Geospatial Foundation ([OSGeo](http://www.osgeo.org/)) and took place close to home, namely in Bonn. Therefore Daniel was extremely happy that <!--more--> his [talk](http://2016.foss4g.org/talks.html#146) "An overview of Docker images for geospatial applications" was voted to be presented by the OSGeo community. Daniel presented an evaluation into the existing containers for FOSS4G software. After an introduction into Docker and some live demos, the takeaway was that everybody should use Docker more, and many different application scenarios (development, demos, training, cloud deployment) exist.

The presentation was very well attended (~ 120 people), albeit taking place in the first session on Friday morning after the conference dinner the night before. [Reactions on Twitter](https://twitter.com/search?q=foss4g%20docker&src=typd) were also quite positive, several [good question](https://twitter.com/foss4g/status/769081504718852119)s were asked, and great discussions followed throughout the day.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Much interest in Docker containerization, <a href="https://twitter.com/hashtag/foss4g?src=hash">#foss4g</a> <a href="https://t.co/i55KphJwKv">pic.twitter.com/i55KphJwKv</a></p>&mdash; michael GOULD (@0mgould) <a href="https://twitter.com/0mgould/status/769075459225219072">August 26, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

The main part of the work is published in the OSGeo wiki: a comprehensive list of Docker containers published by projects or third parties to use a large variety of tools, libraries, or Desktop applications in Docker containers. Check out the list at **[https://wiki.osgeo.org/wiki/DockerImages](https://wiki.osgeo.org/wiki/DockerImages)**. Contributions are welcome!

_How is this related to the o2r project?_ The expertise build up around Docker should be shared with the communities we know. And more concretely, many applications in the geospatial world are build upon services and APIs, so scientific work building upon these APIs will require to archive such services, too. This is a topic we will experiment on in the second year of o2r.

![geocontainers logo](http://geocontainers.org/img/geocontainers-logo.png "geocontainers logo"){:width="100" .img.rightfloat}As some popular projects surprisingly did not have Docker images yet, Daniel started a new independent project [on GitHub](https://github.com/geocontainers/) to provide a place for FOSS4G-related containers and to expand the knowledge and application of containers for geospatial applications: **[geocontainers](http://geocontainers.org/)**. Inspired by [Biodocker](http://biodocker.org/), geocontainers is intended to be a place to experiment and collaborate on containers without any initial rules or guidelines.

All of this is described in detail in [his presentation](http://www.slideshare.net/nuest/docker-foss4g-2016-bonn-public), which is also available as a [video recording](http://ftp5.gwdg.de/pub/misc/openstreetmap/FOSS4G-2016/foss4g-2016-1146-an_overview_of_docker_images_for_geospatial_applications-hd.mp4). Feedback welcome!

[![presentation video screenshot](/public/images/2016-08_foss4g-video-docker.jpg "presentation video screenshot"){:width="600"}](http://ftp5.gwdg.de/pub/misc/openstreetmap/FOSS4G-2016/foss4g-2016-1146-an_overview_of_docker_images_for_geospatial_applications-hd.mp4)

The conference was excellently organized in [a great venue](http://www.worldccbonn.com/en/history.html) which includes the former Plenary Chambers of the Bundestag. Indeed a very special place to meet the people behind the projects of Free and Open Source Software for Geospatial.

![FOSS4G keynote in Bundestag's old Plenary Chamber](/public/images/2016-09_foss4g-plenary-chamber.jpg "FOSS4G keynote in Bundestag's old Plenary Chamber"){:width="600"}