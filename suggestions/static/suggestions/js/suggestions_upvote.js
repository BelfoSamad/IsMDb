$(".up_vote").click(function (e) {
    e.preventDefault();
    if (document.getElementById("user_auth").value === "false")
            window.location.href = "http://http://127.0.0.1:8000/login";
    else {
        var this_ = $(this);
        var upvote_url = this_.attr("data-href");
        console.log(upvote_url);
        var countClass = $("." + this_.attr("id"));
        $.ajax({
            url: upvote_url,
            method: "GET",
            data: {},
            success: function (data) {
                console.log(data);
                countClass.text(data.up_votes + " upvotes")
            }, error: function (error) {
                console.log(error);
                console.log("error");
            }
        });
    }
});
$(".delete").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var delete_url = this_.attr("data-href");
    $.ajax({
        url: delete_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            if (data.deleted) {
                var selector = $(".four-suggs");
                console.log(selector.attr("data-href"));
                selector.load(selector.attr("data-href"));
            }
        }, error: function (error) {
            console.log(error);
        }
    });
});