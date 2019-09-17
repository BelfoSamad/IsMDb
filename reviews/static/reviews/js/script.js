var lastActiveReview, popCarousel, recCarousel;

var instance = M.Tabs.init($(".tabs"), null);

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
        cover_border = "1px 0 0 1px";
        details_border = "0 1px 1px 0";
    } else {
        $(".more-info").css("left", "auto");
        $(".more-info").css("right", "100%");
        cover_border = "0 1px 1px 0";
        details_border = "1px 0 0 1px";
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
    let revs_wrapper = $("#content").find(".reviews-wrapper");
    let elementy = $("#content").find(element);
    let elementy_right = elementy.offset().left + elementy.width() + 400;
    let revs_wrapper_right = revs_wrapper.offset().left + revs_wrapper.width();
    return revs_wrapper_right - elementy_right > 0
}

function isDisplayed(element) {
    return $("#content").find(element).siblings(".more-info").css("width") !== "0px";
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

$("#content").on("click", ".review-cover", function () {
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

function showRating(element, text1, text2) {
    var rating_box = $(element).closest(".com-review").find(".rating-content");
    if (rating_box.hasClass("hidden")) {
        rating_box.removeClass("hidden");
        setTimeout(function () {
            rating_box.removeClass("visually-hidden");
            $(element).find("span").text(text2);
            $(element).find("i").css("transform", "rotate(180deg) translateY(-1px)");
        }, 20);
    } else {
        rating_box.addClass("visually-hidden");
        rating_box.one("transitionend", function () {
            rating_box.addClass("hidden");
            $(element).find("span").text(text1);
            $(element).find("i").css("transform", "rotate(0deg) translateY(0px)");
        });
    }
};

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