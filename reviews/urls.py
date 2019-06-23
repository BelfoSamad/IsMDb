from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.home, name='home'),
    path(r'^movie/', views.review, name='review'),
    url(r'^.*\.html', views.html_loader, name="html-loader"),
    url(r'^autocomplete/', views.autocomplete, name="autocomplete"),
]
