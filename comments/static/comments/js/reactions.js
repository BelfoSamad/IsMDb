$(".add_comment").click(function (e) {
        e.preventDefault();
        if (document.getElementById("user_auth").value === "false")
            window.location.href = "http://http://127.0.0.1:8000/test";
        else {
            var this_ = $(this);
            var id = this_.attr("id");
            var add_comment_url = this_.attr("data-href");
            var title = document.getElementById("id_title");
            var content = document.getElementById("id_content");
            var alcohol = document.getElementById("alcohol");
            var language = document.getElementById("language");
            var lgbtq = document.getElementById("lgbtq");
            var nudity = document.getElementById("nudity");
            var sex = document.getElementById("sex");
            var violence = document.getElementById("violence");
            $.ajax({
                url: add_comment_url,
                method: "GET",
                data: {
                    'title': title.value,
                    'content': content.value,
                    'id': id,
                    'alcohol': alcohol.value,
                    'language': language.value,
                    'lgbtq': lgbtq.value,
                    'nudity': nudity.value,
                    'sex': sex.value,
                    'violence': violence.value
                },
                success: function (data) {
                    console.log(data);
                    if (data.added) {
                        var selector = $(".comments");
                        selector.load(selector.attr("data-href"));
                        $('#id_title').val('');
                        $('#id_content').val('');
                        $('#alcohol').val(0);
                        $('#language').val(0);
                        $('#lgbtq').val(0);
                        $('#nudity').val(0);
                        $('#sex').val(0);
                        $('#violence').val(0);
                        showRating(this, 'Show Review', 'Hide Review');
                    }
                },
                error: function (error) {
                    console.log(error);
                    console.log("error");
                }
            });
        }
    }
);
$(".like").click(function (e) {
        if (document.getElementById("user_auth").value === "false")
            window.location.href = "http://http://127.0.0.1:8000/test";
        else {
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
        }
    }
);
$(".dislike").click(function (e) {
        if (document.getElementById("user_auth").value === "false")
            window.location.href = "http://http://127.0.0.1:8000/test";
        else {
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
        }
    }
);