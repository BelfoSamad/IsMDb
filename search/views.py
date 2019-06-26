from django.shortcuts import render


# Create your views here.
from haystack.generic_views import SearchView

from search.forms import DateRangeSearchForm


class AdvancedSearch(SearchView):
    # template_name = 'reviews/advanced_search.html'
    form_class = DateRangeSearchForm


'''
def advanced_search(request):
    return render(request, 'reviews/advanced_search.html')
'''
