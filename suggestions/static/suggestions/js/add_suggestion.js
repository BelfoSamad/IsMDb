// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("add_suggestion");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
function addSuggestion() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function closeAddSuggestion() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
        document.getElementById("id_title_auto").value = '';
        document.getElementById("id_description").value = '';
    }
}

$(".add_suggestion").click(function (e) {
        e.preventDefault();
        if (document.getElementById("user_auth").val === "false")
            window.location.href = "http://http://127.0.0.1:8000/test";
        else {
            var this_ = $(this);
            var add_suggestion_url = this_.attr("data-href");
            var title = document.getElementById("id_title_auto").value;
            var description = document.getElementById("id_description").value;
            $.ajax({
                url: add_suggestion_url,
                method: "GET",
                data: {
                    'title': title,
                    'description': description
                },
                success: function (data) {
                    console.log(data);
                    modal.style.display = "none";
                },
                error: function (error) {
                    console.log(error);
                }
            });
        }
    }
);