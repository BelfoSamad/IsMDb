from django.conf.urls import url
from suggestions.views import SuggestionsListView

app_name = 'suggestions'

urlpatterns = [
    url(r'^suggestions/$', SuggestionsListView.as_view(), name='suggestions'),
    # url(r'^add_suggestion/$', SuggestionCreateView.as_view(), name='add_suggestion'),
    # url(r'^api/upvote/(?P<id>\d+)$', views.SuggestionUpVote.as_view(), name='upvote'),
]
