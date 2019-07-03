import logging
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, DetailView
from haystack.query import SearchQuerySet
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from IsMDb.utils import convert_to_dataframe
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
            reviews = MovieReview.objects.order_by('pub_date')
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
        recently_added = MovieReview.objects.order_by('pub_date')

        context = {
            'reviews': reviews,
            'popular': popular,
            'recently_added': recently_added,
        }
        template_name = 'reviews/home.html'

    return render(request, template_name, context)


'''
class ReviewsListView(ListView):
    model = MovieReview
    # template_name = 'reviews/reviews.html'
    context_object_name = 'reviews_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casts = Actor.objects.all()
        context['casts'] = casts
        return context
'''


def review(request):
    movie_id = request.GET.get('id', -1)
    movies = MovieReview.objects.filter(id=movie_id)
    template = 'reviews/review.html'
    print(id)
    return render(request, template, {'movies': movies})


'''
class MovieDetailView(DetailView):
    model = MovieReview
    template_name = 'reviews/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.object.title
        qs = MovieReview.objects.all()
        related = getRelated(qs, title)
        context["form"] = CommentForm()
        context["related"] = reversed(MovieReview.objects.filter(title__in=related))
        return context

'''


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('query', ''))
    template = loader.get_template('reviews/autocomplete_template.html')
    return HttpResponse(template.render({'reviews': sqs}, request))


class LikeReview(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        print(id)
        liked = False
        if id != -1:
            obj = MovieReview.objects.get(id=id)
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
        updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)


def get_csv(request):
    qs = MovieReview.objects.all()
    df = convert_to_dataframe(qs, fields=['genre', 'alcohol', 'nudity', 'sex', 'LGBTQ', 'violence', 'language'])
    df.drop()
    print(df.head())
    return render(request, '')
