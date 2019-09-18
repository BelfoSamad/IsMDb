// Get the modal
var report_comment_modal = document.getElementById("ReportCommentModal");

// Get the <span> element that closes the modal
var report_comment_span = document.getElementsByClassName("close_report_comment")[0];

// When the user clicks on the button, open the modal
let comment_id = 0;

function showCommentModal(id) {
    comment_id = id;
    report_comment_modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
// TODO: report_comment_span.onclick = function () {
//     report_comment_modal.style.display = "none";
// }
//-----------------------------------------------------------------------------------------------------
// Get the modal
var report_review_modal = document.getElementById("ReportReviewModal");

// Get the <span> element that closes the modal
var report_review_span = document.getElementsByClassName("close_report_review")[0];

function showReviewModal() {
    report_review_modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
// TODO: report_review_span.onclick = function () {
//     report_review_modal.style.display = "none";
// }

//------------------------------------------------------------------------------------------------------
// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === report_comment_modal) {
        report_comment_modal.style.display = "none";
        report_review_modal.style.display = "none";
    }
}
//----------------------------------------------------------------------------------
$(".report_comment").click(function (e) {
    e.preventDefault();
    if (document.getElementById("user_auth").val === "false")
        window.location.href = "http://http://127.0.0.1:8000/test";
    else {
        var this_ = $(this);
        var report_comment_url = this_.attr("data-href");
        var content = $('#report_comment_content input:radio').val();
        console.log(content);
        console.log(comment_id);
        $.ajax({
            url: report_comment_url,
            method: "GET",
            data: {
                'content': content,
                'id': comment_id
            },
            success: function (data) {
                console.log(data);
                report_comment_modal.style.display = "none";
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
});

$(".report_review").click(function (e) {
    e.preventDefault();
    if (document.getElementById("user_auth").val === "false")
        window.location.href = "http://http://127.0.0.1:8000/test";
    else {
        var this_ = $(this);
        var report_review_url = this_.attr("data-href");
        var content = $('#report_review_content input:radio').val();
        $.ajax({
            url: report_review_url,
            method: "GET",
            data: {
                'content': content,
                'id': document.getElementById("review_id").val
            },
            success: function (data) {
                console.log(data);
                report_comment_modal.style.display = "none";
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
});