import datetime

from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.models import Comment


class CommentsListView(ListView):
    model = Comment
    # template_name = 'comments/comments.html'


class CommentCreateView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        title = request.GET.get('title', None)
        content = request.GET.get('content', None)
        review_id = request.GET.get('id', None)
        Comment.objects.create(title=title, content=content, memberID=user, reviewID_id=review_id,
                               date_added=datetime.datetime.now())
        data = {
            "added": True,
        }
        return Response(data)


class CommentLike(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        print(id)
        liked = False
        if id != -1:
            obj = Comment.objects.get(id=id)
            if user in obj.dislikes.all():
                liked = True
                obj.dislikes.remove(user)
                obj.likes.add(user)
            elif user in obj.likes.all():
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


class CommentDislike(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        print(id)
        disliked = False
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
        updated = True
        data = {
            "updated": updated,
            "liked": disliked
        }
        return Response(data)
