import datetime

from django.contrib.auth.models import User
from notifications.signals import notify
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from comments.models import Comment
from reports.models import ReportReview as ReportRev
from reports.models import ReportComment as ReportComm
from reviews.models import MovieReview
from users.models import Member


class ReportComment(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        content = request.GET.get('content', None)
        comment_id = request.GET.get('id', None)
        ReportComm.objects.create(content=content, memberID=user, commentID_id=comment_id,
                                  date_added=datetime.datetime.now())
        staff = [s for s in Member.objects.all() if
                 s.groups.filter(name='Admin').exists() or s.groups.filter(name='Moderator').exists()]
        comment = Comment.objects.get(id=comment_id)
        print(staff)
        notify.send(user, recipient=staff, verb='Reported Comment', action_object=comment.reviewID)
        data = {
            "Reported": True,
        }
        return Response(data)


class ReportReview(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        content = request.GET.get('content', None)
        review_id = request.GET.get('id', None)
        ReportRev.objects.create(content=content, memberID=user, reviewID_id=review_id,
                                 date_added=datetime.datetime.now())
        staff = [s for s in Member.objects.all() if
                 s.groups.filter(name='Admin').exists() or s.groups.filter(name='Moderator').exists()]
        review = MovieReview.objects.get(id=review_id)
        notify.send(user, recipient=staff, verb='Reported Comment', action_object=review)
        data = {
            "Reported": True,
        }
        return Response(data)
