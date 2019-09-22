//TODO: Change Class Name
var Autocomplete_Suggestion = function (options) {
    this.form_selector = options.form_selector;
    this.url = options.url || '/search/autocomplete/';
    this.delay = parseInt(options.delay || 100);
    this.minimum_length = parseInt(options.minimum_length || 1);
    this.form_elem = null;
    this.query_box = null;
};

Autocomplete_Suggestion.prototype.setup = function () {
    var self = this;

    this.form_elem = $(this.form_selector);
    this.query_box = this.form_elem.find('input[name=title_auto]');

    // Watch the input box.
    this.query_box.on('keyup', function () {
        const query = self.query_box.val();
        if (query.length < self.minimum_length) {
            return false
        }

        self.fetch(query)
    });

    //On selecting a result, populate the search field.
    this.form_elem.on('click', '.results', function () {
        self.query_box.val($(this).text());
        $('.results').remove();
        return false
    })
};

Autocomplete_Suggestion.prototype.fetch = function (query) {
    console.log(query);
    $(".results").load("autocomplete/" + query);
};

$(document).ready(function () {
    window.autocomplete = new Autocomplete_Suggestion({
        form_selector: '.autocomplete-me-suggestions'
    });
    window.autocomplete.setup()
});