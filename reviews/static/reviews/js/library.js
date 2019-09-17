$(".watchlist").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    console.log("test");
    var bookmark_url = this_.attr("data-href");
    $.ajax({
        url: bookmark_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});
$(".review_later").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var review_later_url = this_.attr("data-href");
    $.ajax({
        url: review_later_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});
$(".like_review").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var like_url = this_.attr("data-href");
    $.ajax({
        url: like_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});

function getLibraryList() {
    var library = document.getElementById("library_select").value;
    var sort = document.getElementById("sort_select").value;
    $(".reviews").load("/library/" + library + sort);
}