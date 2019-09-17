//TODO: Change Variables
var Autocomplete = function (options) {
    this.form_selector = options.form_selector;
    this.url = options.url || '/search/autocomplete/';
    this.delay = parseInt(options.delay || 100);
    this.minimum_length = parseInt(options.minimum_length || 1);
    this.form_elem = null;
    this.query_box = null;
};

Autocomplete.prototype.setup = function () {
    var self = this;

    this.form_elem = $(this.form_selector);
    this.query_box = this.form_elem.find('input[name=q1]');

    // Watch the input box.
    this.query_box.on('keyup', function () {
        const query = self.query_box.val();
        if (query.length < self.minimum_length) {
            $(".search-results1").load("search/init");
        }

        self.fetch(query)
    });

    // On selecting a result, populate the search field.
    this.form_elem.on('click', '.search-results1', function () {
        self.query_box.val($(this).text());
        $('.search-results1').remove();
        return false
    })
};

Autocomplete.prototype.fetch = function (query) {
    console.log(query);
    $(".search-results1").load("search/auto_search/" + query);
};

$(document).ready(function () {
    window.autocomplete = new Autocomplete({
        form_selector: '.autocomplete-me1'
    });
    window.autocomplete.setup()
});