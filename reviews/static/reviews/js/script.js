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

popCarousel = new Carousel($(".content-holder").find("#pop-carousel"));
recCarousel = new Carousel($(".content-holder").find("#rec-carousel"));

class CarouselV2 {
    constructor(container) {
        this.container = container;
        this.rightSwipeIcon = this.container.find(".right-arrow");
        this.leftSwipeIcon = this.container.find(".left-arrow");
        this.reviewsWrapper = this.container.find(".elements");
        this.currentReview = 0;
        this.totalReviews = this.reviewsWrapper.children().length;
        this.swipeRightListener = this.rightSwipeIcon.click(this.swipeRight.bind(this));
        this.swipeLeftListener = this.leftSwipeIcon.click(this.swipeLeft.bind(this));
    }

    swipeRight() {
        let currentElement = this.reviewsWrapper.children().eq(this.currentReview);

        currentElement.addClass("visually-hidden");
        currentElement.one("transitionend", function () {
            currentElement.addClass("hidden");
        });
        setTimeout(() => {
            this.currentReview++;
            if (this.currentReview == this.totalReviews) this.currentReview = 0;
            currentElement = this.reviewsWrapper.children().eq(this.currentReview);
            currentElement.removeClass("hidden");
            setTimeout(function () {
                currentElement.removeClass("visually-hidden");
            }, 20);
        }, 800);
    }

    swipeLeft() {
        let currentElement = this.reviewsWrapper.children().eq(this.currentReview);

        currentElement.addClass("visually-hidden");
        currentElement.one("transitionend", function () {
            currentElement.addClass("hidden");
        });
        setTimeout(() => {
            this.currentReview--;
            if (this.currentReview == -1) this.currentReview = this.totalReviews - 1;
            currentElement = this.reviewsWrapper.children().eq(this.currentReview);
            currentElement.removeClass("hidden");
            setTimeout(function () {
                currentElement.removeClass("visually-hidden");
            }, 20);
        }, 1000);
    }
}

displayCarousel = new CarouselV2($("#content").find(".display"));
//setInterval(() => displayCarousel.swipeRight(), 15000)

// function loadHtml(file_name) {
//     console.log("loading: " + file_name);
//     $(".content-holder").scrollTop(0);
//     $(".home-animation").css("height", "calc(100vh - 90px)");
//     switch (file_name) {
//         case "category.html":
//             setTimeout(() => $(".category-holder").load(file_name), 1000);
//             break;
//         case "home.html":
//             setTimeout(() => $(".category-holder").load(file_name), 1000);
//             break;
//         case "reviews.html":
//             setTimeout(() => $(".category-holder").css("height", "0%"), 1000);
//             setTimeout(() => $(".reviews-holder").css("height", "100%"), 1000);
//             setTimeout(() => $(".reviews-holder").load(file_name), 1000);
//             break;
//     }
//     setTimeout(() => $(".home-animation").css("height", "0"), 2000);
//     if (file_name == "home.html") {
//         setTimeout(() => {
//             popCarousel = new Carousel($(".content-holder").find("#pop-carousel"));
//             recCarousel = new Carousel($(".content-holder").find("#rec-carousel"));
//         }, 2000);
//     }
// }

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
        cover_border = "8px 0 0 8px";
        details_border = "0 8px 8px 0";
    } else {
        $(".more-info").css("left", "auto");
        $(".more-info").css("right", "100%");
        cover_border = "0 8px 8px 0";
        details_border = "8px 0 0 8px";
    }
    $(element).find(".film-cover").css("border-radius", cover_border);
    $(element).siblings(".more-info").css("border-radius", details_border);
    $(element).siblings(".more-info").css("width", "400px");
    setTimeout(function () {
        $(element).siblings(".more-info").find(".animation-div").css("height", "0");
    }, 350);
}

function leftShown(element) {
    console.log("leftShown");
    let revs_wrapper = $("#home").find(".reviews-wrapper");
    let elementy = $("#home").find(element);
    let elementy_right = elementy.offset().left + elementy.width() + 400;
    let revs_wrapper_right = revs_wrapper.offset().left + revs_wrapper.width();
    return revs_wrapper_right - elementy_right > 0
}

function isDisplayed(element) {
    return $("#home").find(element).siblings(".more-info").css("width") !== "0px";
}

function empty(element) {
    $(".home-animation").css("height", "calc(100vh - 90px)");
    setTimeout(() => $(element).empty(), 500);
    setTimeout(() => $(".category-holder").css("height", "100%"), 500);
    setTimeout(() => $(".reviews-holder").css("height", "0%"), 500);
    setTimeout(() => $(".home-animation").css("height", "0"), 1000);
}

// loadHtml("home.html");

// Event Listeners
// $("#logo").click(() => loadHtml("home.html"));

// $(".category-holder").on("click", ".go-back-btn", () => loadHtml("home.html"));

// $(".reviews-holder").on("click", ".go-back-btn", () => empty(".reviews-holder"));

// $(".content-holder").on("click", ".category-title", () => loadHtml("category.html"));

// $(".content-holder").on("click", ".see-more", () => loadHtml("category.html"));

// $(".content-holder").on("click", ".view-reviews", () => loadHtml("reviews.html"));

$("#home").on("click", ".review-cover", function () {
    let this_elem = this;
    console.log(!isDisplayed(this_elem));

    if (!isDisplayed(this_elem)) {
        if (lastActiveReview && isDisplayed(lastActiveReview)) {
            hideReviewDetails(lastActiveReview);
            setTimeout(function () {
                if (leftShown($(this_elem).parent())) showReviewDetails(this_elem, "left");
                else showReviewDetails(this_elem, "right");
                lastActiveReview = this_elem;
            }, 700);
        } else {
            if (leftShown($(this_elem).parent())) showReviewDetails(this_elem, "left");
            else showReviewDetails(this_elem, "right");
            lastActiveReview = this_elem;
        }
    } else hideReviewDetails(this_elem);
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
    } else {
        $("#topnav").removeClass("shadow");
    }
});

$(".bell").click(() => {
    console.log("yo")
    var notif_box = $(".dropdown");
    if (notif_box.hasClass("hidden")) {
        notif_box.removeClass("hidden");
        setTimeout(function () {
            notif_box.removeClass("visually-hidden");
        }, 20);
    } else {
        notif_box.addClass("visually-hidden");
        notif_box.one("transitionend", function () {
            notif_box.addClass("hidden");
        });
    }
});

$(".profile-icon").click(() => {
    console.log("yo")
    var notif_box = $(".profile-dropdown");
    if (notif_box.hasClass("hidden")) {
        notif_box.removeClass("hidden");
        setTimeout(function () {
            notif_box.removeClass("visually-hidden");
        }, 20);
    } else {
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

(function ($) {
}(jQuery));