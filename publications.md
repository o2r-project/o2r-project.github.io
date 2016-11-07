---
layout: page
title: Publications
description: Publications in the context of the project Opening Reproducible Research (o2r)
categories:
  - publications
---

<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/x2js/1.2.0/xml2json.min.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.js"></script>

<script src="//cdn.jsdelivr.net/jquery.webui-popover/2.1.15/jquery.webui-popover.min.js"></script>
<link rel="stylesheet" href="//cdn.jsdelivr.net/jquery.webui-popover/2.1.15/jquery.webui-popover.min.css">

<script id="templatePubl" type="x-tmpl-mustache">
{% raw %}
<li>
    <strong><a href="{{crisURL}}" title="CRIS entry of publication">{{title}}</a></strong>{{subtitle}}
    <i>{{ authors }}</i>
    <br>
    {{#hasJournalName}}{{journalName}}{{/hasJournalName}}<i class="editor"> {{publicationType}} {{editor}}</i><i class="editor"> {{series}} {{venue}} {{publicationYear}}</i>
    {{#hasISBN}}ISBN: {{isbn}};{{/hasISBN}}
    {{#hasDoi}}doi: <a href="{{doi}}">{{doi}}</a>;{{/hasDoi}}
    {{#hasURL}}<br><a href="{{url}}">{{url}}</a>{{/hasURL}}
</li>
{% endraw %}
</script>

<script id="templateTalk" type="x-tmpl-mustache">
{% raw %}
<li>
    <a href="#" class="show-pop" title="Abstract" data-placement="bottom" data-content="{{abstract}}"><strong>{{title}}</strong></a> by <i>{{speakers}}</i>
    <br>
    Presented at <a href="{{eventUrl}}" title="event URL">{{event}}</a> ({{organiser}}) on {{date}}, {{venue}}.
    <br>
    {{#hasDoi}}<a href="{{doi}}">{{doi}}</a>;{{/hasDoi}}
    {{#hasSlidesURL}}<a href="{{slidesUrl}}">Download slides</a>{{/hasSlidesURL}}
</li>
{% endraw %}
</script>

<script type="text/javascript">
var x2js = new X2JS();

$(document).ready(function(){
    // get publications
    $.ajax({
        type: "get",
        url: "https://o2r.uni-muenster.de/wwuproxy/forschungaz-rest/ws/public/infoobject/getrelated/Project/9520/PROJ_has_PUBL",
        dataType: "text",
        success: function(data) {
            var publicationsData = x2js.xml_str2json(data).infoObjects;

            var template = $('#templatePubl').html();
            Mustache.parse(template);

            var publications = [];

            $(publicationsData.infoObject).each(function(index, value) {
                if(value._type === "Publication" && value._statusVisible === "true") {
                    var crisId = value._id;
                    var attributes = value.attribute;

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
                                switch(value.data){
                                    case "212":
                                        pubType = "Book";
                                        break;
                                    case "569":
                                        pubType = "Book(editor)";
                                        break;
                                    case "394":
                                        pubType = "Book chapter";
                                        break;
                                    case "570":
                                        pubType = "Article(conference)";
                                        break;
                                    case "1567":
                                        pubType = "Abstract(poster)";
                                        break;
                                    case "210":
                                        pubType = "Article(journal)";
                                        break;
                                    case "1566":
                                        pubType = "Article";
                                        break;
                                    case "1568":
                                        pubType = "Encyclopedia entry";
                                        break;
                                    case "568":
                                        pubType = "Recension";
                                        break;
                                    case "1569":
                                        pubType = "Thesis";
                                        break;
                                    case "211":
                                        pubType = "Report";
                                        break;
                                    case "572":
                                        pubType = "Other";
                                        break;
                                    case "1644":
                                        pubType = "Media";
                                        break;
                                }
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
                        crisId: crisId,
                        crisURL: "https://www.uni-muenster.de/forschungaz/publication/" + crisId + "?lang=en",
                        title: title,
                        authors: authors,
                        subtitle: function() {
                            if(subtitle.length != 0) return ": " + subtitle + ".";
                        },
                        publicationType: function() {
                            if(pubType.length != 0) return pubType + ".";
                        },
                        publicationYear: function() {
                            if(pubYear.length != 0) return pubYear + ".";
                        },
                        hasVenue: function() {
                            return venue.length != 0;
                        },
                        venue: venue,
                        journalName: function() {
                            if(journalName.length != 0) return journalName + ".";
                        },
                        editor: function(){
                            if(editor.length != 0 ) return editor + ".";
                        },
                        series: function(){
                           if(seriesTitle.length != 0) return seriesTitle + ".";
                        },
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

                    publications.push(view);
                } // else not a publication
            });

            publications.sort(function(a,b){
                return b.crisId - a.crisId;
            });

            var list = $("#publicationlist");
            list.empty(); // clear the list to remove the loader

            publications.forEach(function(element, index, array) {
                var output = Mustache.render(template, element);
                list.append(output);
            });
        },
        error: function(xhr, status) {
            $("#publications").html("Error fetching publications: " + status);
        }
    });

    // get talks
    $.ajax({
        type: "get",
        url: "https://o2r.uni-muenster.de/wwuproxy/forschungaz-rest/ws/public/infoobject/getrelated/Project/9520/PROJ_has_TALK",
        dataType: "text",
        success: function(data) {
            var talksData = x2js.xml_str2json(data).infoObjects.infoObject;

            var template = $('#templateTalk').html();
            Mustache.parse(template);

            var talks = [];

            $(talksData).each(function(index, value) {
                if(value._type === "Talk" && value._statusVisible === "true") {
                    var crisId = value._id;
                    var attributes = value.attribute;

                    var title, date, event, venue, organiser, abstract, keywords, doi, slidesUrl, speakers, eventUrl, year;

                    $(attributes).each(function(index, value) {
                        switch(value._name) {
                            case "Title":
                                if(!title && value.data) {
                                    title = value.data;
                                }
                                break;
                            case "Date of talk":
                                date = value.data;
                                break;
                            case "Name of event":
                                event = value.data;
                                break;
                            case "Venue of event":
                                venue = value.data;
                                break;
                            case "Organiser of event":
                                organiser = value.data;
                                break;
                            case "Abstract":
                                if(!abstract && value.data) {
                                    abstract = value.data;
                                }
                                break;
                            case "Keywords":
                                keywords = value.data;
                                break;
                            case "DOI":
                                doi = value.data;
                                break;
                            case "URL of slides":
                                slidesUrl = value.data;
                                break;
                            case "Speakers":
                                speakers = value.data;
                                break;
                            case "URL of event":
                                eventUrl = value.data;
                                break;
                            case "Year of talk":
                                year = value.data;
                                break;
                        }
                    });

                    var view = {
                        title: title,
                        date: date,
                        event: event,
                        venue: venue,
                        organiser: organiser,
                        abstract: abstract,
                        keywords: keywords,
                        doi: doi,
                        hasDoi: function() {
                            return doi.length != 0;
                        },
                        slidesUrl: slidesUrl,
                        hasSlidesURL: function() {
                            return slidesUrl.length != 0;
                        },
                        speakers: speakers,
                        eventUrl: eventUrl,
                        year: year
                    };

                    talks.push(view);
                } // else not a talk
            });

            talks.sort(function(a,b){
                // Turn your strings into dates, and then subtract them
                // to get a value that is either negative, positive, or zero.
                return new Date(b.date) - new Date(a.date);
            });

            var list = $("#talklist");
            list.empty(); // clear the list to remove the loader

            talks.forEach(function(element, index, array) {
                var output = Mustache.render(template, element);
                list.append(output);
            });

            // active popovers on the links with popover content
            $('a.show-pop').filter(function() {
                return $(this).attr('data-content');
            }).webuiPopover({width: 600});
        },
        error: function(xhr, status) {
            $("#talks").html("Error fetching talks: " + status);
        }
    });
});
</script>

<div id="publications">
    <ul id="publicationlist">
        <li><img alt="loading image" class="center" src="{{site.baseurl}}public/images/loading.gif" width="32" /></li>
    </ul>
</div>

<h1>Talks</h1>
<p>(newest first)</p>

<div id="talks">
    <ul id="talklist">
        <li><img alt="loading image" class="center" src="{{site.baseurl}}public/images/loading.gif" width="32" /></li>
    </ul>
</div>

<div class="attribution">
    <p>Publications are loaded dynamically from the University of Münster's platform "Research from A-Z", see <a href="https://www.uni-muenster.de/forschungaz/project/9520?lang=en">project description</a>.</p>
</div>
