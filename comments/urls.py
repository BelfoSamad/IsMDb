from django.conf.urls import url
from comments import views
from comments.views import CommentsListView, CommentCreateView

app_name = 'comments'

urlpatterns = [
    url(r'^comment/$', CommentsListView.as_view(), name='comments'),
    url(r'^api/like/(?P<id>\d+)$', views.CommentLike.as_view(), name='like'),
    url(r'^api/dislike(?P<id>\d+)$', views.CommentDislike.as_view(), name='dislike'),
    url(r'^api/add/$', CommentCreateView.as_view(), name='add_comment'),
]
