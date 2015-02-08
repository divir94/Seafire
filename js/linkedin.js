var loadData = function() {
    IN.API.Profile("me")
        .fields(["id", "firstName", "lastName", "pictureUrl", "headline", "publicProfileUrl", "industry"])
        .result(function (result) {
            profile = result.values[0];
            profHTML = "<p><a href=\"" + profile.publicProfileUrl + "\">";
            profHTML += "<img class=img_border align=\"left\" src=\"" + profile.pictureUrl + "\"></a>";
            profHTML += "<a href=\"" + profile.publicProfileUrl + "\">";
            profHTML += "<h2 class=myname>" + profile.firstName + " " + profile.lastName + "</a> </h2>";
            profHTML += "<span class=myheadline>" + profile.industry + "</span>";
            $("#profile").html(profHTML);
        });
};

var getHeadlines = function() {
     IN.API.Connections("me").fields("headline").result(processHeadlines);
};

var processHeadlines = function(json) {
    words = ""
    $.each( json.values, function( key, value ) {
        words += value.headline + ' ' ;
    });
    words = words.replace(/\W+/g, " ").removeStopWords().split(' ')

    var histogramMap = {};
    for(var i=0, len=words.length; i<len; i++){
        var key = words[i];
        histogramMap[key] = (histogramMap[key] || 0) + 1;
    }

    cloud_words = []
    $.each( histogramMap, function( key, value ) {
        if (value>1) cloud_words.push({'text': key, 'size': Math.log(value*1.5)*20});
    });

    makeWordCloud(cloud_words);
};

var linkedinMain = function() {
    getHeadlines();
}

