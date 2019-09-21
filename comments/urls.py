from django.conf.urls import url
from comments import views

app_name = 'comments'

urlpatterns = [
    url(r'^api/like/(?P<id>\d+)/(?P<movie_id>\d+)$', views.CommentLike.as_view(), name='like'),
    url(r'^api/dislike/(?P<id>\d+)$', views.CommentDislike.as_view(), name='dislike'),
    url(r'^api/add_comment/$', views.CommentCreateView.as_view(), name='add_comment'),
    url(r'^comments/(?P<id>\d+)$', views.load_comments, name='comments'),
]
