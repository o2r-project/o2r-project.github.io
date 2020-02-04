---
layout: page
title: 📄 Publications
description: Publications in the context of the project Opening Reproducible Research (o2r)
categories:
  - publications
exclude_from_all_pages: true
---

<script type="text/javascript" src="{{ '/public/js/jquery.js' | absolute_url }}"></script><!-- //cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.js -->
<script type="text/javascript" src="{{ '/public/js/xml2json.min.js' | absolute_url }}"></script><!-- //cdnjs.cloudflare.com/ajax/libs/x2js/1.2.0/xml2json.min.js -->
<script type="text/javascript" src="{{ '/public/js/mustache.js' | absolute_url }}"></script><!-- //cdnjs.cloudflare.com/ajax/libs/mustache.js/2.2.1/mustache.js -->

<script type="text/javascript" src="{{ '/public/js/jquery.webui-popover.min.js' | absolute_url }}"></script><!-- //cdn.jsdelivr.net/jquery.webui-popover/2.1.15/jquery.webui-popover.min.js -->
<link rel="stylesheet" href="{{ '/public/css/jquery.webui-popover.min.css' | absolute_url }}"><!-- //cdn.jsdelivr.net/jquery.webui-popover/2.1.15/jquery.webui-popover.min.css -->

<script id="templatePublication" type="x-tmpl-mustache">
{% raw %}
<li>
    {{#hasBadge}}<img src="{{badge_url}}" alt="publication badge" class="publicationBadge"/>{{/hasBadge}}<strong><a href="{{crisURL}}" title="CRIS entry of publication">{{title}}</a></strong>{{subtitle}}
    <i>{{ authors }}</i>
    <br />
    <i class="editor">{{publicationType}} {{journalName}} {{editor}}</i><i class="editor"> {{seriesTitle}} {{venue}} {{publicationYear}}</i>
    {{#hasISBN}}ISBN:&nbsp;{{isbn}};{{/hasISBN}}
    {{#hasDoi}}<strong>doi:&nbsp;<a href="{{#hasNoDoiUrl}}https://doi.org/{{/hasNoDoiUrl}}{{doi}}">{{doi}}</a></strong>;{{/hasDoi}}
    {{#hasURL}}<br><a href="{{url}}">{{url}}</a>{{/hasURL}}
</li>
{% endraw %}
</script>

<script id="templateTalk" type="x-tmpl-mustache">
{% raw %}
<li>
    <a href="#" class="show-pop" title="Abstract" data-placement="bottom" data-content="{{abstract}}"><strong>{{title}}</strong></a> by <i>{{speakers}}</i>
    <br />
    Presented at <a href="{{eventUrl}}" title="event URL">{{event}}</a> ({{organiser}}) on {{date}}, {{venue}}.
    <br />
    {{#hasDoi}}<strong>doi:&nbsp;<a href="https://doi.org/{{doi}}">{{doi}}</a></strong>;{{/hasDoi}}
    {{#hasSlidesURL}}<a href="{{slidesUrl}}">Download slides</a>{{/hasSlidesURL}}
</li>
{% endraw %}
</script>

<script type="text/javascript">
var x2js = new X2JS();

parsePublications = function(data) {
    var publicationsData = x2js.xml_str2json(data).infoObjects;

    var publications = [];

    $(publicationsData.infoObject).each(function(index, value) {
        if(value._type === "Publication" && value._statusVisible === "true") {
            var crisId = value._id;
            var attributes = value.attribute;

            var title, reviewed, venue, subtitle, journalName, pubYear, authors, pubType, seriesTitle, editor, isbn, doi, url, comments, badge_url;

            $(attributes).each(function(index, value) {
                switch(value._name) {
                    case "Title":
                        title = value.data;
                        break;
                    case "Peer reviewed":
                        if(value.data === "1570") {
                            reviewed = true;
                        }
                        if(value.data === "1571") {
                            reviewed = false;
                        }
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

            if((pubType === "Other" || pubType.includes("Article"))
                && (url.includes("arxiv")
                    || journalName.toLowerCase().includes("preprint")
                    || seriesTitle.toLowerCase().includes("preprint"))) {
                badge_url = "https://img.shields.io/badge/article-preprint-ff69b4.svg";
            }

            if(pubType.includes("Article") && reviewed) {
                badge_url = "https://img.shields.io/badge/article-peer--reviewed-brightgreen.svg";
            }

            var view = {
                crisId: crisId,
                badge_url: badge_url,
                hasBadge: function() {
                    return badge_url != undefined;
                },
                crisURL: "https://www.uni-muenster.de/forschungaz/publication/" + crisId + "?lang=en",
                title: title,
                authors: authors,
                subtitle: function() {
                    if(subtitle.length != 0) return ":&nbsp;" + subtitle + ".";
                },
                publicationType: function() {
                    if(pubType.length != 0) return pubType + ".";
                },
                publicationYear: function() {
                    if(pubYear.length != 0) return pubYear + ".";
                },
                venue: venue,
                journalName: function() {
                    if(journalName.length != 0) return journalName + ".";
                },
                editor: function(){
                    if(editor.length != 0 ) return editor + ".";
                },
                seriesTitle: function(){
                    if(seriesTitle.length != 0) return seriesTitle + ".";
                },
                hasISBN: function() {
                    return isbn.length != 0;
                },
                isbn: isbn,
                hasDoi: function() {
                    return doi.length != 0;
                },
                hasNoDoiUrl: function() {
                    return !doi.includes('doi.org');
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

    return(publications);
}

parseTalks = function(data) {
    var talksData = x2js.xml_str2json(data).infoObjects.infoObject;

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

    return(talks);
}

$(document).ready(function(){

    var publications = [];
    var talks = [];

    $.when(
        $.ajax({
            type: "get",
            url: "https://o2r.uni-muenster.de/wwuproxy/forschungaz-rest/ws/public/infoobject/getrelated/Project/9520/PROJ_has_PUBL",
            dataType: "text",
            success: function(data) {
                o2rPubs = parsePublications(data);
                publications = publications.concat(o2rPubs);
            },
            error: function(xhr, status) {
                $("#publications").html("<p>Error fetching publications: " + status + "</p><p><strong>Please visit <a href=\"https://www.uni-muenster.de/forschungaz/project/9520\">https://www.uni-muenster.de/forschungaz/project/9520</a></strong></p>");
            }
        }),
        $.ajax({
            type: "get",
            url: "https://o2r.uni-muenster.de/wwuproxy/forschungaz-rest/ws/public/infoobject/getrelated/Project/12343/PROJ_has_PUBL",
            dataType: "text",
            success: function(data) {
                o2r2Pubs = parsePublications(data);
                publications = publications.concat(o2r2Pubs);
            },
            error: function(xhr, status) {
                $("#publications").html("<p>Error fetching publications: " + status + "</p><p><strong>Please visit <a href=\"https://www.uni-muenster.de/forschungaz/project/12343\">https://www.uni-muenster.de/forschungaz/project/12343</a></strong></p>");
            }
        }),
        $.ajax({
            type: "get",
            url: "https://o2r.uni-muenster.de/wwuproxy/forschungaz-rest/ws/public/infoobject/getrelated/Project/9520/PROJ_has_TALK",
            dataType: "text",
            success: function(data) {
                o2rTalks = parseTalks(data);
                talks = talks.concat(o2rTalks);
            },
            error: function(xhr, status) {
                $("#publications").html("<p>Error fetching publications: " + status + "</p><p><strong>Please visit <a href=\"https://www.uni-muenster.de/forschungaz/project/9520\">https://www.uni-muenster.de/forschungaz/project/9520</a></strong></p>");
            }
        }),
        $.ajax({
            type: "get",
            url: "https://o2r.uni-muenster.de/wwuproxy/forschungaz-rest/ws/public/infoobject/getrelated/Project/12343/PROJ_has_TALK",
            dataType: "text",
            success: function(data) {
                o2r2Talks = parseTalks(data);
                talks = talks.concat(o2r2Talks);
            },
            error: function(xhr, status) {
                $("#publications").html("<p>Error fetching publications: " + status + "</p><p><strong>Please visit <a href=\"https://www.uni-muenster.de/forschungaz/project/12343\">https://www.uni-muenster.de/forschungaz/project/12343</a></strong></p>");
            }
        })
    ).then( function(){
        publications.sort(function(a,b){
            return b.crisId - a.crisId;
        });
        talks.sort(function(a,b){
            // Turn your strings into dates, and then subtract them
            // to get a value that is either negative, positive, or zero.
            return new Date(b.date) - new Date(a.date);
        });

        var pubList = $("#publicationlist");
        var talkList = $("#talklist");
        // clear the list to remove the loader
        pubList.empty();
        talkList.empty();

        var templatePubs = $('#templatePublication').html();
        Mustache.parse(templatePubs);
        var templateTalks = $('#templateTalk').html();
        Mustache.parse(templateTalks);

        publications.forEach(function(element, index, array) {
            var output = Mustache.render(templatePubs, element);
            pubList.append(output);
        });
        talks.forEach(function(element, index, array) {
            var output = Mustache.render(templateTalks, element);
            talkList.append(output);
        });

        // activate popovers on the links with popover content
        $('a.show-pop').filter(function() {
            return $(this).attr('data-content');
        }).webuiPopover({width: 600});
    });
});
</script>

<div id="publications">
    <ul id="publicationlist">
        <li><img alt="loading image" class="center" src="/public/images/loading.gif" width="32" /></li>
        <li>If loading the publications does not work, please check your adblockers and privacy plug-ins - they must allow requests to o2r.uni-muenster.de. Alternatively visit <strong><a href="https://www.uni-muenster.de/forschungaz/project/9520">https://www.uni-muenster.de/forschungaz/project/9520</a></strong> and <strong><a href="https://www.uni-muenster.de/forschungaz/project/12343">https://www.uni-muenster.de/forschungaz/project/12343</a></strong>.</li>
    </ul>
</div>

<h1>Talks</h1>
<p>(newest first)</p>

<div id="talks">
    <ul id="talklist">
        <li><img alt="loading image" class="center" src="/public/images/loading.gif" width="32" /></li>
        <li>If loading the talks does not work, please check your adblockers and privacy plug-ins - they must allow requests to o2r.uni-muenster.de. Alternatively visit <strong><a href="https://www.uni-muenster.de/forschungaz/project/9520">https://www.uni-muenster.de/forschungaz/project/9520</a></strong> and <strong><a href="https://www.uni-muenster.de/forschungaz/project/12343">https://www.uni-muenster.de/forschungaz/project/12343</a></strong>.</li>
    </ul>
</div>

<div class="attribution">
    <p>Publications are loaded dynamically from the University of Münster's platform "Research from A-Z", see project descriptions for <a href="https://www.uni-muenster.de/forschungaz/project/9520?lang=en">o2r</a> and <a href="https://www.uni-muenster.de/forschungaz/project/12343">o2r2</a>.</p>
</div>
