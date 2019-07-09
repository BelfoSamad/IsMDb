# Website URL Structure

- 'ismdb.com': (view: get_reviews, template: home.html, context: popular && recently added && explore)
    - 'ismdb.com/category/(slug)': (view: get_category, template: category.html, context: popular || recently added || explore based on the slug)
    - 'ismdb.com/review/(slug)': (view: MovieDetailView, template: review.html, context: movie that with the slug = slug)
    - 'ismdb.com/api/like/(id)': (view: LikeReview no template or context needed)
- 'ismdb.com/suggestion': (view: SuggestionsListView, template: suggestions.html, context: suggestions)
    - 'ismdb.com/suggestions/add_suggestion': (view: SuggestionCreateView, template: add_suggestion.html, context: No Context, + redirect to suggestions list)
    - 'ismdb.com/suggestions/api/upvote/(id)': (view: SuggestionUpVote, no template or context needed)
- 'ismdb.com/search': (view: AdvancedSearch, template: advanced_search.html, no context needed)
    - 'ismdb.com/search/autocomplete': (view: autocomplete, template: autocomplete_template.html loaded in search bar, context: search results)

+ 'ismdb.com/comments/(id)': (view: load_comments, template: comments.html loaded in review.html, context: comments of the review with id = id)
+ 'ismdb.com/api/like/(id)': (view: CommentLike, no template or context needed)
+ 'ismdb.com/api/dislike/(id)': (view: CommentDislike, no template or context needed)
+ 'ismdb.com/api/add_comment': (view: CommentCreateView, no template or context needed)

+ 'ismdb.com/admin': admin

+ ...