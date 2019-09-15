$(".bookmark_review").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var bookmark_url = this_.attr("data-href");
    $.ajax({
        url: bookmark_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            if (data.bookmarked) {
                this_.val("Bookmarked")
            }
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
    var countClass = $("." + this_.attr("id"));
    $.ajax({
        url: like_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            if (data.liked) {
                countClass.text(data.likes)
            }
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});