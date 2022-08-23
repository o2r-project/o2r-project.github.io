---
layout: page
title: ⚙️ Deployment
description: Project results
---

<br>

Find a list of all **papers and presentations** at <https://o2r.info/publications/>.

Try the **online demo** at [https://o2r.uni-muenster.de](https://o2r.uni-muenster.de) and if you are a developer find the web API endpoint at [https://o2r.uni-muenster.de/api/v1/](https://o2r.uni-muenster.de/api/v1/).

Try it out on your own machine with the [**reference implementation**](/2017/10/31/reference-implementation/) (only Docker required!):

`git clone https://github.com/o2r-project/reference-implementation`
`docker-compose up`

Watch a short **video** of our platform prototype (turn on subtitles!):

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Vy9b3pIWPd0?rel=0" frameborder="0" allowfullscreen></iframe>

<br>

To cite the reference implementation please use

> Nüst, Daniel, 2018. Reproducibility Service for Executable Research Compendia: Technical Specifications and Reference Implementation. Zenodo. doi:[10.5281/zenodo.2203844](http://doi.org/10.5281/zenodo.2203844)

## Software

Learn more about our projects on [Open Hub](https://www.openhub.net/orgs/o2r) and [GitHub](https://github.com/o2r-project), where we currently have <span id="gh-stats-repo-count">[NA]</span> repositories with <span id="gh-stats-forks-count">[NA]</span> forks using <span id="gh-stats-languages-count">[NA]</span> languages.

<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.js"></script>
<script type="text/javascript">
$(document).ready(function(){
    // get repo count
    $.ajax({
        type: "get",
        url: "https://api.github.com/orgs/o2r-project",
        success: function(data) {
            var repo_count = data.public_repos;
            $("#gh-stats-repo-count").html(repo_count);
        },
        error: function(err, status) {
            console.log("Error getting repo count from GitHub API: " + err);
        }
    });

    // get languages and forks
    $.ajax({
        type: "get",
        url: "https://api.github.com/users/o2r-project/repos?sort=pushed&per_page=100",
        success: function(data) {
            let languages = new Set();
            let forks = 0;
            data.forEach(function(item) {
                languages.add(item.language);
                forks += item.forks_count;
            });
            $("#gh-stats-languages-count").html(languages.size);
            $("#gh-stats-forks-count").html(forks);
        },
        error: function(err, status) {
            console.log("Error getting repo details from GitHub API: " + err);
        }
    });
});
</script>

<!--
<script type="text/javascript" src="https://www.openhub.net/orgs/o2r/widgets/portfolio_projects_activity?format=js"></script>
-->
