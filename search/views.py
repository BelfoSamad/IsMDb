from django.http import HttpResponse
from django.template import loader
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

from reviews.models import MovieReview

search_result = None


class AdvancedSearch(SearchView):
    template_name = 'search/advanced_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global search_result
        search_result = MovieReview.objects.all()
        context['reviews'] = search_result
        return context


def init(request):
    global search_result
    search_result = MovieReview.objects.all()
    template = loader.get_template('search/advanced_search_results.html')
    return HttpResponse(template.render({'reviews': search_result}, request))


def auto_search(request, query):
    global search_result
    search_res = search_result.filter(title__contains=query)
    search_result = search_res
    template = loader.get_template('search/advanced_search_results.html')
    return HttpResponse(template.render({'reviews': search_result}, request))


def auto_filter(request, max_year, min_year, max_time, min_time, genre, alcohol, language, lgbtq, nudity, sex,
                violence):
    global search_result
    results = [result for result in search_result if
               (result.year >= max_year) and (result.year <= min_year) and (result.time >= max_time) and (
                       result.time <= min_time) and (result.alcohol >= alcohol) and (result.alcohol <= alcohol) and (
                       result.language >= language) and (result.language <= language) and (
                       result.lgbtq >= lgbtq) and (result.lgbtq <= lgbtq) and (result.nudity >= nudity) and (
                       result.nudity <= nudity) and (result.sex >= sex) and (result.sex <= sex) and (
                       result.violence >= violence) and (result.violence <= violence)]
    template = loader.get_template('search/advanced_search_results.html')
    return HttpResponse(template.render({'reviews': results}, request))


def autocomplete(request, query):
    sqs = SearchQuerySet().autocomplete(content_auto=query)
    template = loader.get_template('search/autocomplete_template.html')
    return HttpResponse(template.render({'reviews': sqs}, request))
