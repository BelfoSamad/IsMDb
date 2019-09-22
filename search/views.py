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
        genres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        context['reviews'] = search_result
        context['genres'] = genres
        # Notification:
        if self.request.user.is_authenticated:
            context['notifications'] = self.request.user.notifications.unread()
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


def auto_filter(request, max_year, min_year, max_time, min_time, genres, max_alcohol, min_alcohol, max_language,
                min_language, max_lgbtq, min_lgbtq, max_nudity, min_nudity, max_sex, min_sex, max_violence,
                min_violence):
    global search_result
    if genres == 'NAN':
        g = []
    else:
        g = genres.split('_')

    results = []
    for result in search_result:
        if (int(max_year) >= result.year >= int(min_year)) and (int(max_time) >= result.time >= int(min_time)) and (
                (int(max_alcohol) / 10) >= result.alcohol >= (int(min_alcohol) / 10)) and (
                (int(max_language) / 10) >= result.language >= (int(min_language) / 10)) and (
                (int(max_lgbtq) / 10) >= result.LGBTQ >= (int(min_lgbtq) / 10)) and (
                (int(max_nudity) / 10) >= result.nudity >= (int(min_nudity) / 10)) and (
                (int(max_sex) / 10) >= result.sex >= (int(min_sex) / 10)) and (
                (int(max_violence) / 10) >= result.violence >= (int(min_violence) / 10)) and (
                all(elem in get_genres(result) for elem in g)):
            results.append(result)
    template = loader.get_template('search/advanced_search_results.html')
    return HttpResponse(template.render({'reviews': results}, request))


def autocomplete(request, query):
    sqs = SearchQuerySet().autocomplete(content_auto=query)
    template = loader.get_template('search/autocomplete_template.html')
    return HttpResponse(template.render({'reviews': sqs}, request))


def get_genres(result):
    genre_choices = ((1, 'Action'),
                     (2, 'Adventure'),
                     (3, 'Animation'),
                     (4, 'Comedy'),
                     (5, 'Crime'),
                     (6, 'Drama'),
                     (7, 'Fantasy'),
                     (8, 'Historical'),
                     (9, 'Horror'),
                     (10, 'Mystery'),
                     (11, 'Political'),
                     (12, 'Romance'),
                     (13, 'Satire'),
                     (14, 'Sci-Fi'))
    choices = dict(genre_choices)
    result_genres = []
    for x in result.genre:
        result_genres.append(choices[int(x)])
    return result_genres
