from django.conf.urls import url
from . import views

app_name = 'reviews'

urlpatterns = [
    url(r'^$', views.get_reviews, name='reviews'),
    url(r'^category/(?P<category>[-\w]+)/$', views.get_category, name='reviews'),
    url(r'^review/(?P<slug>[-\w]+)/$', views.MovieDetailView.as_view(), name='review'),
    url(r'^api/like/(?P<id>\d+)$', views.LikeReview.as_view(), name='like'),
]
