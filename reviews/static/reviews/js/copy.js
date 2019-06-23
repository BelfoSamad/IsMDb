var lastActiveReview, popCarousel, recCarousel;

class Carousel {
    constructor(container) {
        this.container = container;
        this.rightSwipeIcon = this.container.find(".swipe-right");
        this.leftSwipeIcon = this.container.find(".swipe-left");
        this.reviewsWrapper = this.container.find(".reviews-wrapper");
        this.reviews = container.find(".reviews");
        this.leftValue = 0;
        this.swipeRightListener = this.rightSwipeIcon.click(this.swipeRight.bind(this));
        this.swipeLeftListener = this.leftSwipeIcon.click(this.swipeLeft.bind(this));
    }
    swipeRight() {
        let revs_right = this.reviews.offset().left + this.reviews.width();
        let revs_wrapper_right = this.reviewsWrapper.offset().left + this.reviewsWrapper.width();
        let difference = revs_right - revs_wrapper_right;
        this.leftValue = difference > 205 ? this.leftValue - 205 : this.leftValue - difference;
        this.swipe();
    }
    swipeLeft() {
        let revs_left = this.reviews.offset().left;
        let revs_wrapper_left = this.reviewsWrapper.offset().left;
        let difference = revs_wrapper_left - revs_left;
        this.leftValue = difference > 205 ? this.leftValue + 205 : this.leftValue + difference;
        this.swipe();
    }
    swipe() {
        if (lastActiveReview && isDisplayed(lastActiveReview))
            hideReviewDetails(lastActiveReview);
        this.reviews.css("left", this.leftValue + "px")
    }
}

function loadHtml(file_name) {
    console.log("loading: " + file_name);
    $(".home-animation").css("height", "calc(100vh - 90px)");
    setTimeout(() => $(".content-holder").load(file_name), 1000);
    setTimeout(() => $(".home-animation").css("height", "0"), 2000);
    if (file_name == "home.html") {
        setTimeout(() => {
            popCarousel = new Carousel($(".content-holder").find("#pop-carousel"));
            recCarousel = new Carousel($(".content-holder").find("#rec-carousel"));
        }, 2000);
    }
}

function hideReviewDetails(element) {
    console.log("hideReviewDetails");
    $(element).find(".film-cover").css("border-radius", "1px");
    $(element).siblings(".more-info").find(".animation-div").css("height", "100%");
    setTimeout(function () {
        $(element).siblings(".more-info").css("width", "0");
    }, 300);
}

function showReviewDetails(element, direction) {
    let cover_border = "";
    let details_border = "";
    if (direction == "left") {
        $(".more-info").css("right", "auto");
        $(".more-info").css("left", "100%");
        cover_border = "10px 0 0 10px";
        details_border = "0 5px 5px 0";
    } else {
        $(".more-info").css("left", "auto");
        $(".more-info").css("right", "100%");
        cover_border = "0 10px 10px 0";
        details_border = "5px 0 0 5px";
    }
    $(element).find(".film-cover").css("border-radius", cover_border);
    $(element).siblings(".more-info").css("border-radius", details_border);
    $(element).siblings(".more-info").css("width", "400px");
    setTimeout(function () {
        $(element).siblings(".more-info").find(".animation-div").css("height", "0");
    }, 350);
}

function leftShown(element) {
    console.log("leftShown")
    let revs_wrapper = $("#home").find(".reviews-wrapper");
    let elementy = $("#home").find(element);
    let elementy_right = elementy.offset().left + elementy.width() + 400;
    let revs_wrapper_right = revs_wrapper.offset().left + revs_wrapper.width();
    return revs_wrapper_right - elementy_right > 0
}

function isDisplayed(element) {
    return $("#home").find(element).siblings(".more-info").css("width") !== "0px";
}
loadHtml("home.html");

// Event Listeners
$("#logo").click(() => loadHtml("home.html"));

$(".content-holder").on("click", ".category-title", () => loadHtml("category.html"));

$(".content-holder").on("click", ".see-more", () => loadHtml("category.html"));

$(".content-holder").on("click", ".view-reviews", () => loadHtml("reviews.html"));

$("#home").on("click", ".reviews-cover", () => {
    let this_elem = this;
    console.log(!isDisplayed(this_elem))

    if (!isDisplayed(this_elem)) {
        if (lastActiveReview && isDisplayed(lastActiveReview)) {
            hideReviewDetails(lastActiveReview);
            setTimeout(function () {
                if (leftShown($(this_elem).parent())) showReviewDetails(this_elem, "left");
                else showReviewDetails(this_elem, "right");
                lastActiveReview = this_elem;
            }, 700);
        }
        else {
            if (leftShown($(this_elem).parent())) showReviewDetails(this_elem, "left");
            else showReviewDetails(this_elem, "right");
            lastActiveReview = this_elem;
        }
    }

    else hideReviewDetails(this_elem);
});

$(".search-icon").click(() => {
    if ($(".search-input").css("width") === "0px") $(".search-input").focus();
    else {
        // Not working..
        $(".search-input").focusout(function (event) {
            $(event.target).focus();
            return false;
        });
    }
});

$(".content-holder").scroll(() => {
    var scrollPos = $(".content-holder").scrollTop();
    if (scrollPos > 0) {
        $("#topnav").addClass("shadow");
    }
    else {
        $("#topnav").removeClass("shadow");
    }
});

$(".bell-icon").click(() => {
    var notif_box = $(".c-notifications");
    if (notif_box.hasClass("hidden")) {
        notif_box.removeClass("hidden");
        setTimeout(function () {
            notif_box.removeClass("visually-hidden");
        }, 20);
    }
    else {
        notif_box.addClass("visually-hidden");
        notif_box.one("transitionend", function () {
            notif_box.addClass("hidden");
        });
    }
});
//$(".settings-wrapper").hide();

$(".set-icon").click(() => {
    $(".settings-wrapper").toggle();
    $(".settings-wrapper .settings").css("left", "76%");
});

$(".close-icon").click(() => {
    $(".settings-wrapper").toggle();
    $(".settings-wrapper .settings").css("left", "100%");
});

/**
$("#email-username").focusout(function () {
    if ($(this).text() == '') {
        $(this).css("border-bottom", "none");
        $(this).css("border-bottom", "1px solid blue");
        $(this).siblings("span").css("opacity", "0");
    }
    else {
        $(this).siblings("span").css("opacity", "100");
    }
}) */

(function ($) {}(jQuery));