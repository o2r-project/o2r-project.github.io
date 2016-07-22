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

            var list = $("#publicationlist");
            $(publications).each(function(index, value) {
                if(value.infoObject._type === "Publication") {
                    var attributes = value.infoObject.attribute;
                    
                    var title, venue, subtitle, journalName, pubYear, authors, pubType, seriesTitle, editor, isbn, doi, url, comments;


                    $(attributes).each(function(index, value) {

                        switch(value._name) {
                            case "Title":
                                title = value.data;
                                break;
                            case "Venue":
                                venue = value.data;
                                break;
                            case "Subtitle":
                                subtitle = value.data;
                                break;
                            case "Journal name":
                                journalName = value.data;
                                break;
                            case "Publication year":
                                pubYear = value.data;
                                break;
                            case "Authors":
                                authors = value.data;
                                break;
                            case "Publication type":
                                pubType = value.additionalInfo;
                                break;
                            case "Title of series":
                                seriesTitle = value.data;
                                break;
                            case "Editor":
                                editor = value.data;
                                break;
                            case "ISBN": 
                                isbn = value.data;
                                break;
                            case "DOI":
                                doi = value.data;
                                break;
                            case "URL":
                                url = value.data;
                                break;
                            case "Comments":
                                comments = value.data;
                                break;
                                

                        }
                    });
                    var content = "<li><a href='" + url + "'>" + title + "</a>";
                    if(subtitle.length != 0) content += ": " + subtitle + ".";

                    content += "<br><i>" + authors + "</i>";

                    content += "<br>";
                    if(pubType.length != 0) content += pubType +" ";
                    if(pubYear.lenght != 0) content += pubYear + " ";
                    if(venue.length != 0) content += venue;
                    if(comments.length != 0) content += ". " + comments + ".";

                    content += "<br>";
                    if(journalName.length != 0) content += journalName;
                    if(editor.length != 0) content += "<i class='editor'>" + editor + "</i>"; 
                    if(seriesTitle.length != 0) content += "<span class='editor'>. <i>" + seriesTitle + "</i></span>";

                    content += "<br>";
                    if(isbn.length != 0 ) content += "ISBN: " + isbn + " ";
                    if(doi.length != 0) content += "DOI: <a href='" + doi + "'>" + doi + "</a>";
                    content += "</li>";

                    list.append(content);
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
