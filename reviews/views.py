from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from IsMDb.recommendation_engine.content_based_filtering.related_reviews import get_related
from comments.forms import CommentForm
from reviews.models import MovieReview


def get_reviews(request):
    template = 'reviews/home.html'
    popular = MovieReview.objects.order_by('likes')
    recently_added = MovieReview.objects.order_by('-pub_date')
    explore = MovieReview.objects.order_by('title')
    context = {
        'popular_reviews': popular,
        'recently_added_reviews': recently_added,
        'explore_reviews': explore
    }
    return render(request, template, context)


def get_category(request, category):
    template = 'reviews/category.html'
    reviews = None
    if category == 'popular':
        reviews = MovieReview.objects.order_by('likes')
    elif category == 'recently_added':
        reviews = MovieReview.objects.order_by('-pub_date')
    elif category == 'explore':
        reviews = MovieReview.objects.order_by('title')

    context = {
        'reviews': reviews,
        'category': category
    }
    return render(request, template, context)


class MovieDetailView(DetailView):
    model = MovieReview
    template_name = 'reviews/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.object.title
        qs = MovieReview.objects.all()
        related = get_related(qs, title)
        context["form"] = CommentForm()
        context["related"] = reversed(MovieReview.objects.filter(title__in=related))
        return context


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
