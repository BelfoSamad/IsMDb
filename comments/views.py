import datetime

from django.shortcuts import render, get_object_or_404
from notifications.signals import notify
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.models import Comment
from reviews.models import MovieReview


def load_comments(request, id):
    object = get_object_or_404(MovieReview, id=id)
    return render(request, 'comments/comments.html', {'object': object})


class CommentCreateView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        title = request.GET.get('title', None)
        content = request.GET.get('content', None)
        review_id = request.GET.get('id', None)
        alcohol = request.GET.get('alcohol', None)
        language = request.GET.get('language', None)
        lgbtq = request.GET.get('lgbtq', None)
        nudity = request.GET.get('nudity', None)
        sex = request.GET.get('sex', None)
        violence = request.GET.get('violence', None)
        Comment.objects.create(title=title, content=content, memberID=user, reviewID_id=review_id,
                               alcohol=alcohol, language=language, LGBTQ=lgbtq, nudity=nudity, sex=sex,
                               violence=violence, date_added=datetime.datetime.now())
        data = {
            "added": True,
        }
        return Response(data)


class CommentLike(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, movie_id=None):
        user = self.request.user
        print('in')
        liked = False
        likes = 0
        if id != -1:
            obj = Comment.objects.get(id=id)
            movie = MovieReview.objects.get(id=movie_id)
            if user in obj.dislikes.all():
                liked = True
                obj.dislikes.remove(user)
                obj.likes.add(user)
                notify.send(user, recipient=obj.memberID, verb='Liked Your Comment On', action_object=movie)
            elif user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
                notify.send(user, recipient=obj.memberID, verb='Liked Your Comment On', action_object=movie)
            likes = obj.likes.count()
        updated = True
        data = {
            "updated": updated,
            "liked": liked,
            "likes": likes
        }
        return Response(data)


class CommentDislike(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        user = self.request.user
        print(id)
        disliked = False
        dislikes = 0
        likes = 0
        if id != -1:
            obj = Comment.objects.get(id=id)
            if user in obj.likes.all():
                disliked = True
                obj.dislikes.add(user)
                obj.likes.remove(user)
            elif user in obj.dislikes.all():
                disliked = False
                obj.dislikes.remove(user)
            else:
                disliked = True
                obj.dislikes.add(user)
            dislikes = obj.dislikes.count()
            likes = obj.likes.count()
        updated = True
        data = {
            "updated": updated,
            "disliked": disliked,
            "dislikes": dislikes,
            "likes": likes
        }
        return Response(data)
