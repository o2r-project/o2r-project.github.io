---
layout: page
title: Publications
description: Publications in the context of the project Opening Reproducible Research (o2r)
categories:
  - publications
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/x2js/1.2.0/xml2json.min.js"></script>

<script type="text/javascript">
var x2js = new X2JS();

$(document).ready(function(){
    $.ajax({
        type: "get",
        url: "https://crossorigin.me/https://www.uni-muenster.de/forschungaz-rest/ws/public/infoobject/getrelated/Project/9520/PROJ_has_PUBL",
        dataType: "text",
        success: function(data) {
            var publications = x2js.xml_str2json(data).infoObjects;
            console.log(JSON.stringify(publications));

            var list = $("#publicationlist");
            $(publications).each(function(index, value) {
                if(value.infoObject._type === "Publication") {
                    var attributes = value.infoObject.attribute;
                    
                    var title, venue;
                    $(attributes).each(function(index, value) {
                        console.log(value);

// TODO use templating, maybe http://json2html.com/ ??

                        switch(value._name) {
                            case "Title":
                                title = value.data;
                                break;
                            case "Venue":
                                venue = value.data;
                        }
                    });

                    list.append("<li>" + title + " @ " + venue + "</li>");
                }
            });
        },
        error: function(xhr, status) {
            $("#publications").html("Error fetching publications: " + status);
        }
    });

});
</script>


<div id="publications">
    <ul id="publicationlist">
    </ul>
</div>

<div class="attribution">
Publications are loaded dynamically from the University of Münster's platform "Research from A-Z", see <a href="https://www.uni-muenster.de/forschungaz/project/9520?lang=en">project description</a>.
</div> 
