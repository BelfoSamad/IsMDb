from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.home, name='home'),
    # url(r'^$', views.ReviewsListView.as_view(), name='reviews'),
    path(r'^movie/', views.review, name='review'),
    # url(r'^(?P<slug>[-\w]+)/$', views.MovieDetailView.as_view(), name='review'),
    url(r'^autocomplete/', views.autocomplete, name="autocomplete"),
]
