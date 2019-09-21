from django.conf.urls import url

from . import views

app_name = 'reviews'

urlpatterns = [
    url(r'^$', views.get_reviews, name='reviews'),
    url(r'^category/(?P<category>[-\w]+)/$', views.get_category, name='category'),
    url(r'^load_library/(?P<library>[-\w]+)/(?P<sort>[-\w]+)$', views.load_library, name='load_library'),
    url(r'^library/(?P<library>[-\w]+)/(?P<sort>[-\w]+)$', views.get_library, name='get_library'),
    url(r'^review/(?P<slug>[-\w]+)/$', views.MovieDetailView.as_view(), name='review'),
    url(r'^api/like/(?P<id>\d+)$', views.LikeReview.as_view(), name='like'),
    url(r'^api/bookmark/(?P<id>\d+)$', views.BookmarkReview.as_view(), name='bookmark'),
    url(r'^api/review_later/(?P<id>\d+)$', views.ReviewLater.as_view(), name='review_later')
]
