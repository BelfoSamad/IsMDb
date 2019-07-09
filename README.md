# Website URL Structure

- 'ismdb.com':
    - <b>view</b>: get_reviews
    - <b>template</b>: home.html
    - <b>context</b>: popular, recently added, explore (list of moviereview)
- 'ismdb.com/category/(slug)':
    - <b>view</b>: get_category
    - <b>template</b>: category.html
    - <b>context</b>: popular or recently added or explore based on the slug (list of moviereview)
- 'ismdb.com/review/(slug)':
    - <b>view</b>: MovieDetailView
    - <b>template</b>: review.html
    - <b>context</b>: movie with the slug = slug (moviereview)
- 'ismdb.com/api/like/(id)':
    - <b>view</b>: LikeReviewn
    - no template or context needed
----------------------------------------------------------------------------------------------------------
- 'ismdb.com/suggestion': 
    - <b>view</b>: SuggestionsListView
    - <b>template</b>: suggestions.html
    - <b>context</b>: suggestions (list of suggestion)
- 'ismdb.com/suggestions/add_suggestion':
    - <b>view</b>: SuggestionCreateView,
    - <b>template</b>: add_suggestion.html
    - <b>context</b>: No Context
    + redirect to suggestions list
- 'ismdb.com/suggestions/api/upvote/(id)':
    - <b>view</b>: SuggestionUpVote
    - no template or context needed
----------------------------------------------------------------------------------------------------------
- 'ismdb.com/search':
    - <b>view</b>: AdvancedSearch
    - <b>template</b>: advanced_search.html
    - <b>context</b>: No Context
- 'ismdb.com/search/autocomplete':
    - <b>view</b>: autocomplete
    - <b>template</b>: autocomplete_template.html loaded in search bar
    - <b>context</b>: search results (list of moviereview)
----------------------------------------------------------------------------------------------------------
+ 'ismdb.com/comments/(id)':
    - <b>view</b>: load_comments
    - <b>template</b>: comments.html loaded in review.html
    - <b>context</b>: comment list of the review with id = id
+ 'ismdb.com/api/like/(id)':
    - <b>view</b>: CommentLike
    - no template or context needed
+ 'ismdb.com/api/dislike/(id)':
    - <b>view</b>: CommentDislike
    - no template or context needed
+ 'ismdb.com/api/add_comment':
    - <b>view</b>: CommentCreateView
    - no template or context needed
----------------------------------------------------------------------------------------------------------
+ 'ismdb.com/admin': admin
----------------------------------------------------------------------------------------------------------
+ ...
----------------------------------------------------------------------------------------------------------

# Infos:

- slug: additional variable in the link with the name of the category (popular, recently_added, explore) or the title of the movie slugified (eg: Toy Story -> toy-story-2019)
- id: additional variable in the link with the id of the movie or suggestions (depends on the link)

- links with api: used only for actions that doesn't need context or template like (liking, disliking, creating comment) - it uses (DjangoRestFramework)
