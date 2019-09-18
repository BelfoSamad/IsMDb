from django.conf.urls import url
from users import views


# SET THE NAMESPACE!
app_name = 'users'

# Be careful setting the name to just /login use user login instead!
urlpatterns = [
    url(r'^api/bookmark/(?P<id>\d+)$', views.BookmarkReview.as_view(), name='bookmark'),
    url(r'^login/$', views.signup, name='bookmarks'),
]
