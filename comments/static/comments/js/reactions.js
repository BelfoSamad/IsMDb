$(".add_comment").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var id = this_.attr("id");
    var add_comment_url = this_.attr("data-href");
    var title = document.getElementById("id_title").value;
    var content = document.getElementById("id_content").value;
    var alcohol = document.getElementById("id_alcohol").value;
    var language = document.getElementById("id_language").value;
    var lgbtq = document.getElementById("id_lgbtq").value;
    var nudity = document.getElementById("id_nudity").value;
    var sex = document.getElementById("id_sex").value;
    var violence = document.getElementById("id_violence").value;

    $.ajax({
        url: add_comment_url,
        method: "GET",
        data: {
            'title': title,
            'content': content,
            'id': id,
            'alcohol': alcohol,
            'language': language,
            'lgbtq': lgbtq,
            'nudity': nudity,
            'sex': sex,
            'violence': violence
        },
        success: function (data) {
            console.log(data);
            if (data.added) {
                const selector = $(".comments");
                const url = selector.attr("id");
                selector.load(url);
            }
        },
        error: function (error) {
            console.log(error);
            console.log("error");
        }
    })
    ;
});
$(".like").click(function (e) {
    var this_ = $(this);
    var like_url = this_.attr("data-href");
    var likes = $("." + this_.attr("id") + "-like");
    var dislikes = $("." + this_.attr("id") + "-dislike");
    $.ajax({
        url: like_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            likes.text(data.likes);
            dislikes.text(data.dislikes);
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});
$(".dislike").click(function (e) {
    var this_ = $(this);
    var dislike_url = this_.attr("data-href");
    var likes = $("." + this_.attr("id") + "-like");
    var dislikes = $("." + this_.attr("id") + "-dislike");
    $.ajax({
        url: dislike_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            likes.text(data.likes);
            dislikes.text(data.dislikes);
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});