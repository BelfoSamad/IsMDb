from django.http import HttpResponse
from django.template import loader
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

from search.forms import DateRangeSearchForm


class AdvancedSearch(SearchView):
    template_name = 'search/advanced_search.html'
    form_class = DateRangeSearchForm


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('query', ''))
    template = loader.get_template('search/autocomplete_template.html')
    return HttpResponse(template.render({'reviews': sqs}, request))
