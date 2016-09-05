---
layout: page
title: Publications
description: Publications in the context of the project Opening Reproducible Research (o2r)
categories:
  - publications
---

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/x2js/1.2.0/xml2json.min.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.js"></script>

<script id="template" type="x-tmpl-mustache">
{% raw %}
<li><strong><a href="{{crisURL}}" title="CRIS entry of publication">{{title}}</a></strong>{{subtitle}}.
<i>{{ authors }}</i>.
<br>
{{#hasJournalName}}{{journalName}}. {{/hasJournalName}}<i class="editor"> {{editor}}</i>.<i class="editor"> {{series}}</i>. {{#hasVenue}} {{venue}}.{{/hasVenue}}
{{#hasISBN}}ISBN: {{isbn}};{{/hasISBN}}
{{#hasDoi}}doi: <a href="{{doi}}">{{doi}}</a>;{{/hasDoi}}
{{#hasURL}}<br><a href="{{url}}">{{url}}</a>{{/hasURL}}
</li>
{% endraw %}
</script>

<script type="text/javascript">
var x2js = new X2JS();

$(document).ready(function(){
    $.ajax({
        type: "get",
        url: "https://crossorigin.me/https://www.uni-muenster.de/forschungaz-rest/ws/public/infoobject/getrelated/Project/9520/PROJ_has_PUBL",
        dataType: "text",
        success: function(data) {
            var publications = x2js.xml_str2json(data).infoObjects;

            var template = $('#template').html();
            Mustache.parse(template);

            var list = $("#publicationlist");
            $(publications).each(function(index, value) {
                if(value.infoObject._type === "Publication" && value.infoObject._statusVisible === "true") {
                    var crisId = value.infoObject._id;
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


                    var view = {
                        crisURL: "https://www.uni-muenster.de/forschungaz/publication/" + crisId + "?lang=en",
                        title: title,
                        authors: authors,
                        subtitle: function() {
                            if(subtitle.length != 0) return ": " + subtitle;
                        },
                        publicationType: function() {
                            if(pubType.length != 0) return pubType + " ";
                        },
                        publicationYear: function() {
                            if(pubType.length != 0) return pubYear + " ";
                        },
                        hasVenue: function() {
                            return venue.length != 0;
                        },
                        venue: venue,
                        journalName: function() {
                            if(journalName.length != 0) return journalName + ".";
                        },
                        editor: editor,
                        series: seriesTitle,
                        hasISBN: function() {
                            return isbn.length != 0;
                        },
                        isbn: isbn,
                        hasDoi: function() {
                            return doi.length != 0;
                        },
                        doi: doi,
                        hasURL: function() {
                            return url != 0;
                        },
                        url: url
                    };
                    var output = Mustache.render(template, view);

                    //if(comments.length != 0) content += ". " + comments + ".";

                    list.empty(); // clear the list to remove the loader
                    list.append(output);
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
        <li><img alt="loading image" class="center" src="{{site.baseurl}}public/images/loading.gif" width="32" /></li>
    </ul>
</div>

<div class="attribution">
Publications are loaded dynamically from the University of Münster's platform "Research from A-Z", see <a href="https://www.uni-muenster.de/forschungaz/project/9520?lang=en">project description</a>.
</div> 
