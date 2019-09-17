$(".add_comment").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var id = this_.attr("id");
    var add_comment_url = this_.attr("data-href");
    var title = "test";
        //document.getElementById("id_title").value;
    var content = document.getElementById("id_content").value;
    var alcohol = 2.5;
        //document.getElementById("id_alcohol").value;
    var language = 4.2;
        //document.getElementById("id_language").value;
    var lgbtq = 1;
        //document.getElementById("id_lgbtq").value;
    var nudity = 1;
        //document.getElementById("id_nudity").value;
    var sex = 3;
        //document.getElementById("id_sex").value;
    var violence = 2;
        //document.getElementById("id_violence").value;

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
                // const selector = $(".comments");
                // const url = selector.attr("id");
                // selector.load(url);
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
    var likes = document.getElementById("like_" + this_.attr("id"));
    $.ajax({
        url: like_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            likes.innerHTML = data.likes;
        }, error: function (error) {
            console.log(error);
        }
    });
});
$(".dislike").click(function (e) {
    var this_ = $(this);
    var dislike_url = this_.attr("data-href");
    var likes = document.getElementById("like_" + this_.attr("id"));
    $.ajax({
        url: dislike_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            likes.innerHTML = data.likes;
        }, error: function (error) {
            console.log(error);
        }
    });
});