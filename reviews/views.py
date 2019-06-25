import logging
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DetailView
from haystack.query import SearchQuerySet

from reviews.models import MovieReview, Actor


def home(request):
    logger = logging.getLogger(__name__)
    global context
    category_name = request.GET.get('category', None)
    review_name = request.GET.get('reviews', None)

    if category_name is not None:
        if category_name == 'popular':
            # Get Popular
            reviews = MovieReview.objects.all()
            context = {
                'name': 'Popular',
                'reviews': reviews
            }
        elif category_name == 'recently_added':
            reviews = MovieReview.objects.order_by('date_created')
            context = {
                'name': 'Recently Added',
                'reviews': reviews
            }
        elif category_name == 'explore':
            reviews = MovieReview.objects.all
            context = {
                'name': 'Explore',
                'reviews': reviews
            }
        template_name = 'reviews/category.html'
    elif review_name is not None:
        # review_name = urllib.parse.unquote(review_name)
        review = MovieReview.objects.filter(id=review_name)
        context = {
            'reviews': review
        }
        template_name = 'reviews/review.html'
    else:
        reviews = MovieReview.objects.all()
        popular = MovieReview.objects.all()
        recently_added = MovieReview.objects.order_by('date_created')

        context = {
            'reviews': reviews,
            'popular': popular,
            'recently_added': recently_added,
        }
        template_name = 'reviews/home.html'

    return render(request, template_name, context)


def html_loader(request):
    load_template = request.path.split('/')[-1]
    template = loader.get_template('reviews/' + load_template)

    reviews = MovieReview.objects.all()
    popular = MovieReview.objects.all()
    recently_added = MovieReview.objects.order_by('date_created')
    movie_cast = MovieReview.objects.filter('directors')
    return HttpResponse(template.render({'reviews': reviews, 'popular': popular,
                                         'recently_added': recently_added, 'casts': movie_cast},
                                        request))


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('query', ''))
    template = loader.get_template('reviews/autocomplete_template.html')
    return HttpResponse(template.render({'reviews': sqs}, request))


def review(request):
    movie_id = request.GET.get('id', -1)
    movies = MovieReview.objects.filter(id=movie_id)
    template = 'reviews/review.html'
    print(id)
    return render(request, template, {'movies': movies})


class ReviewsListView(ListView):
    model = MovieReview
    # template_name = 'reviews/reviews.html'
    context_object_name = 'reviews_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casts = Actor.objects.all()
        context['casts'] = casts
        return context


class MovieDetailView(DetailView):
    model = MovieReview
    # template_name = 'reviews/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
