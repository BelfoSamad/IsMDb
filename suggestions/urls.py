from django.conf.urls import url
from suggestions import views

app_name = 'suggestions'

urlpatterns = [
    url(r'^$', views.SuggestionsListView.as_view(), name='suggestions'),
    url(r'^my_suggestions/$', views.load_my_suggestions, name='my_suggestions'),
    url(r'^api/add_suggestion/$', views.SuggestionCreateView.as_view(), name='add_suggestion'),
    url(r'^api/upvote/(?P<id>\d+)$', views.SuggestionUpVote.as_view(), name='upvote'),
    url(r'^api/delete/(?P<id>\d+)$', views.SuggestionDelete.as_view(), name='delete'),
]
