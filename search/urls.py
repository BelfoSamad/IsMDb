from django.conf.urls import url
from search import views

app_name = 'search'

urlpatterns = [
    url(r'^auto_complete/$', views.autocomplete, name="autocomplete"),
    url(r'^$', views.AdvancedSearch.as_view(), name='advanced_search'),
]
