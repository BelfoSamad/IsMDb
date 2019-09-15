$(".up_vote").click(function (e) {
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
            if (data.up_voted) {
                countClass.text(data.up_votes)
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