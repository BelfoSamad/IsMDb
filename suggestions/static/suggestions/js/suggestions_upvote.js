$(".up_vote").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var upvote_url = this_.attr("data-href");
    console.log(upvote_url);
    var countClass = $("#" + this_.attr("id"));
    $.ajax({
        url: upvote_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            if (data.up_voted) {
                countClass.text("Upvotes" + data.up_votes)
            }
        }, error: function (error) {
            console.log(error);
            console.log("error");
        }
    });
});
$(".up_vote_result").click(function (e) {
    e.preventDefault();
    var this_ = $(this);
    var like_url = this_.attr("data-href");
    $.ajax({
        url: like_url,
        method: "GET",
        data: {},
        success: function (data) {
            console.log(data);
            //TODO: Go Back into Suggestions W/ Message
        }, error: function (error) {
            console.log(error);
        }
    });
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
        }, error: function (error) {
            console.log(error);
        }
    });
});