from django.conf.urls import url
from search import views

app_name = 'search'

urlpatterns = [
    url(r'autocomplete/(?P<query>\w+)$', views.autocomplete, name="autocomplete"),
    url(r'auto_search/(?P<query>\w+)$', views.auto_search, name="auto_search"),
    url(
        r'auto_filter/(?P<max_year>\d+)/(?P<min_year>\d+)/(?P<max_time>\d+)/(?P<min_time>\d+)/(?P<max_alcohol>\d+)/(?P<min_alcohol>\d+)/(?P<max_language>\d+)/(?P<min_language>\d+)/(?P<max_lgbtq>\d+)/(?P<min_lgbtq>\d+)/(?P<max_nudity>\d+)/(?P<min_nudity>\d+)/(?P<max_sex>\d+)/(?P<min_sex>\d+)/(?P<max_violence>\d+)/(?P<min_violence>\d+)/(?P<genres>\w+)$',
        views.auto_filter, name="auto_filter"),
    url(r'init$', views.init, name="init"),
    url(r'^$', views.AdvancedSearch.as_view(), name='advanced_search'),
]
