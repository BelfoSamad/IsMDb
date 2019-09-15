from django.conf.urls import url
from search import views

app_name = 'search'

urlpatterns = [
    url(r'autocomplete/(?P<query>\w+)$', views.autocomplete, name="autocomplete"),
    url(r'auto_search/(?P<query>\w+)$', views.auto_search, name="auto_search"),
    url(
        r'auto_filter?max_year=(?P<max_year>\w+)&min_year=(?P<min_year>\w+)&max_time=(?P<max_time>\w+)'
        r'&min_time=(?P<min_time>\w+)&alcohol=(?P<alcohol>\w+)&language=(?P<language>\w+)&lgbtq=(?P<lgbtq>\w+)'
        r'&nudity=(?P<nudity>\w+)&sex=(?P<sex>\w+)&violence=(?P<violence>\w+)$',
        views.auto_filter, name="auto_filter"),
    url(r'^$', views.AdvancedSearch.as_view(), name='advanced_search'),
]
