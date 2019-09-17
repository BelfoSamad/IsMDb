from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from IsMDb.recommendation_engine.content_based_filtering.criteria_similarity import get_criteria_similarity
from IsMDb.recommendation_engine.content_based_filtering.related_reviews import get_related
from comments.forms import CommentForm
from reviews.models import MovieReview
from users.models import Member


def get_reviews(request):
    template = 'reviews/home.html'
    popular = MovieReview.objects.order_by('likes')
    recently_added = MovieReview.objects.order_by('-pub_date')
    explore = MovieReview.objects.order_by('title')

    if request.user.is_authenticated:
        context = {
            'popular_reviews': popular,
            'recently_added_reviews': recently_added,
            'explore_reviews': explore,
            'notifications': request.user.notifications.unread()
        }
    else:
        context = {
            'popular_reviews': popular,
            'recently_added_reviews': recently_added,
            'explore_reviews': explore,
        }

    return render(request, template, context)


def get_category(request, category):
    template = 'reviews/category.html'
    reviews = None
    if category == 'recently_added':
        reviews = MovieReview.objects.order_by('-pub_date')
    elif category == 'popular':
        reviews = MovieReview.objects.order_by('likes')
    elif category == 'explore':
        reviews = MovieReview.objects.order_by('title')

    if request.user.is_authenticated:
        context = {
            'reviews': reviews,
            'category': category,
            'notifications': request.user.notifications.unread()
        }
    else:
        context = {
            'reviews': reviews,
            'category': category
        }

    return render(request, template, context)


def get_library(request, library, sort):
    template = 'reviews/library.html'
    reviews = None
    user = request.user
    member = get_object_or_404(Member, id=user.id)
    if library == 'your-watchlist':
        if sort == 'alphabetical-order':
            reviews = member.watchlist.order_by('title')
        elif sort == 'date-order-oldest':
            reviews = member.watchlist.order_by('pub-date')
        elif sort == 'date-order-newest':
            reviews = member.watchlist.order_by('-pub_date')
    elif library == 'liked':
        if sort == 'alphabetical-order':
            reviews = member.review_likes.order_by('title')
        elif sort == 'date-order-oldest':
            reviews = member.review_likes.order_by('pub-date')
        elif sort == 'date-order-newest':
            reviews = member.review_likes.order_by('-pub_date')
    elif library == 'review-later':
        if sort == 'alphabetical-order':
            reviews = member.review_later.order_by('title')
        elif sort == 'date-order-oldest':
            reviews = member.review_later.order_by('pub-date')
        elif sort == 'date-order-newest':
            reviews = member.review_later.order_by('-pub_date')

    if request.user.is_authenticated:
        context = {
            'reviews': reviews,
            'notifications': request.user.notifications.unread()
        }
    else:
        context = {
            'reviews': reviews
        }
    return render(request, template, context)


def load_library(request, library, sort):
    template = 'reviews/library_results.html'
    reviews = None
    user = request.user
    member = get_object_or_404(Member, id=user.id)
    if library == 'your-watchlist':
        if sort == 'alphabetical-order':
            reviews = member.watchlist.order_by('title')
        elif sort == 'date-order-oldest':
            reviews = member.watchlist.order_by('pub-date')
        elif sort == 'date-order-newest':
            reviews = member.watchlist.order_by('-pub_date')
    elif library == 'liked':
        if sort == 'alphabetical-order':
            reviews = member.review_likes.order_by('title')
        elif sort == 'date-order-oldest':
            reviews = member.review_likes.order_by('pub-date')
        elif sort == 'date-order-newest':
            reviews = member.review_likes.order_by('-pub_date')
    elif library == 'review-later':
        if sort == 'alphabetical-order':
            reviews = member.review_later.order_by('title')
        elif sort == 'date-order-oldest':
            reviews = member.review_later.order_by('pub-date')
        elif sort == 'date-order-newest':
            reviews = member.review_later.order_by('-pub_date')

    if request.user.is_authenticated:
        context = {
            'reviews': reviews,
            'notifications': request.user.notifications.unread()
        }
    else:
        context = {
            'reviews': reviews
        }
    return render(request, template, context)


class MovieDetailView(DetailView):
    model = MovieReview
    template_name = 'reviews/review.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Cast
        context["actors"] = self.object.cast_actor.all()
        context["writers"] = self.object.cast_writer.all()
        context["directors"] = self.object.cast_director.all()

        # Comment
        comments = self.object.comment_set.all()
        context["comments"] = reversed(comments)

        # Notification:
        if self.request.user.is_authenticated:
            context['notifications'] = self.request.user.notifications.unread()

        # Related Movies
        title = self.object.title
        qs = MovieReview.objects.all()

        # Recommendation based on likes
        # user = self.request.user
        # member = get_object_or_404(Member, id=user.id)
        # related = get_criteria_similarity(qs, member.review_likes)

        related = get_related(qs, title)

        related_qs = []
        for x in related:
            related_qs.extend(MovieReview.objects.filter(title=x))
        context["related"] = related_qs

        # Form
        context["form"] = CommentForm()

        return context


class LikeReview(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
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


class BookmarkReview(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        bookmarked = False
        if id != -1:
            obj = MovieReview.objects.get(id=id)
            if obj in user.watchlist.all():
                bookmarked = False
                user.watchlist.remove(obj)
            else:
                bookmarked = True
                user.watchlist.add(obj)
        updated = True
        data = {
            "updated": updated,
            "liked": bookmarked
        }
        return Response(data)


class ReviewLater(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        bookmarked = False
        if id != -1:
            obj = MovieReview.objects.get(id=id)
            if obj in user.review_later.all():
                bookmarked = False
                user.review_later.remove(obj)
            else:
                bookmarked = True
                user.review_later.add(obj)
        updated = True
        data = {
            "updated": updated,
            "liked": bookmarked
        }
        return Response(data)
