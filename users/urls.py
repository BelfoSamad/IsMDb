from django.conf.urls import url
from django.urls import path

from users import views
# SET THE NAMESPACE!
from users.views import user_login, user_logout

app_name = 'users'

# Be careful setting the name to just /login use user login instead!
urlpatterns = [
    url(r'^api/bookmark/(?P<id>\d+)$', views.BookmarkReview.as_view(), name='bookmark'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
