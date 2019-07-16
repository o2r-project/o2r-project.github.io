---
layout: post
title: "Summer break technical post: ORCID OAuth with passport.js"
categories:
  - implementation
  - orcid
  - node.js
author: 'Daniel Nüst, Jan Koppe'
---

With the University in a rather calm state during summer, the o2r team continues to work on the first prototypes for testing and demonstrating our ideas. This is the first post on a technical topic, and we will occasionally write about topics that are not related to the scientific work but either kept us busy for some time or might be useful to others.

Last week o2r team member Jan struggled with the implementation of the **login feature** for a [Node.js](https://nodejs.org/en) [microservice](https://en.wikipedia.org/wiki/Microservices). _Why would we bother with that?_
<!--more-->Because we want to share our prototypes publicly and invite you to try them out, but at the same time not have to worry about one of your most valuable possessions: your password.

Therefore we decided early on to rely on [three legged **OAuth 2.0**](http://oauthbible.com/#oauth-2-three-legged) for handling user authentication. We opted for [**ORCID**](http://orcid.org/) as the authorization server because it is the most widespread identification for researchers today[^1], and because of the potential for useful integrations in the future[^2].

The solution[^3] required to dig a bit deeper into the code of the used libraries, namely [passport.js](http://passportjs.org/) with the plugin [passport-oauth2](https://github.com/jaredhanson/passport-oauth2). Jan summarizes everything nicely [in **this Gist**](https://gist.github.com/JanKoppe/1491e37d1022c77a286087e6c81d6092) and the working implementation is part of our component [o2r-bouncer](https://github.com/o2r-project/o2r-bouncer). The ORCID support team was even so kind to include our solution on their [code examples page](https://members.orcid.org/api/code-examples) and we shared it with the [ORCID API Users mailing list](https://groups.google.com/forum/#!topic/orcid-api-users/RRyhC-2L64U) in the hope that future developers will find this information helpful.

So in the end, a full day of work to figure out two missing lines of code, but still many days saved on bullet-proofing standalone authentication and password storage.

[^1]: The used libraries would allow us to quickly add more authorization services, such as Google or GitHub.
[^2]: Wouldn't you like to have a research container be automatically added to your publication list?
[^3]: In a nutshell, the `passReqToCallback` option must be enabled when creating the `OAuth2Strategy` and the [used callback function](https://github.com/o2r-project/o2r-bouncer/blob/dd3416e8a349aaa4a57ab8b061fe1556dd6d7041/index.js#L47) must include 6 arguments. Only then the [function with the largest number of arguments](https://github.com/jaredhanson/passport-oauth2/blob/1eb4f22d5f6ca8bc6b08856f91779f67e5082fe0/lib/strategy.js#L184) is used and the content of the accessToken-request answer, which includes the ORCID id and user name, is accessible in your own code. They can be found in the `params` parameter of the function, not as part of `profile` as one is used to with other OAuth servers. This seems to be a slight deviation from the standard by the ORCID folks.