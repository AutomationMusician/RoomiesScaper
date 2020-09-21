(function() {
    var articles = document.getElementsByTagName("article");
    var links = [];
    articles.forEach(article => {
        links.push(article.children[0].href);
    });
    var output = links.join("\n");
    copy(output);
    return output;
})();