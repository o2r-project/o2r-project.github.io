---
layout: post
title: "Summer break technical post: ORCID OAuth with passport.js"
categories:
  - implementation
  - orcid
  - node.js
---

With the University in a rather calm state during summer, the o2r team continues to work on the first prototypes for testing and demonstrating our ideas. This is the first post on a technical topic, and we will occassionally publish on things that are not really related with the scientific work but nevertheless kept us busy for some time or might be useful to others.

Last week o2r team member Jan struggled with the implementation of the **login feature** for a Node.js microservice. _Why would we bother with that?_
<!--more-->Because we want to share our prototypes publicly and invite you to try them out, but at the same time not have to worry about one of your most valuable possessions: your password.

Therefore we decided early on to rely on [three legged **OAuth** 2.0](http://oauthbible.com/#oauth-2-three-legged). We then opted for [**ORCID**](http://orcid.org/) as the authorization server because it is the most widespread identification for researchers today[^1], and because of the potential for useful integrations in the future[^2].

The solution required to dig a bit deeper into the code of the used libraries, namely [passport.js](http://passportjs.org/) with the plugin [passport-oauth2](https://github.com/timshadel/passport-oauth2-public-client). Jan summarizes everything nicely [in **this Gist**](https://gist.github.com/JanKoppe/1491e37d1022c77a286087e6c81d6092) and the full working implementation is part of our microservice [o2r-bouncer](https://github.com/o2r-project/o2r-bouncer). The ORCID support team was even so kind to link to it from their [code examples page](https://members.orcid.org/api/code-examples).

In a nutshell, the `passReqToCallback` option must be enabled when creating the `OAuth2Strategy`. Only then the function with the largest number of arguments can be used and the content of the accessToken-request answer, which includes the ORCID id and user name, is accessible in your own code. They can be found in the `params` function parameter, not as part of `profile` as you are used to with other OAuth servers. This seems to be a slight deviation from the standard by the ORCID folks.
So in the end, a full day of work to figure out two missing lines of code, but still many days saved on bullet-proofing a standalone authentication.

We also shared this detail with the [ORCID API Users mailing list](https://groups.google.com/forum/#!topic/orcid-api-users/RRyhC-2L64U) in the hope that future developers will find this information helpful.


[^1]: The used libraries would allow us to quickly add more authorization services, such as Google or GitHub.
[^2]: Wouldn't you like to have a research container be automatically added to your publication list?