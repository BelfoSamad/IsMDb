import datetime

from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from reports.models import ReportReview as ReportRev
from reports.models import ReportComment as ReportComm


class ReportComment(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        content = request.GET.get('content', None)
        review_id = request.GET.get('id', None)
        ReportComm.objects.create(content=content, memberID=user, reviewID_id=review_id,
                                  date_added=datetime.datetime.now())
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
        comment_id = request.GET.get('id', None)
        ReportRev.objects.create(content=content, memberID=user, commentID_id=comment_id,
                                 date_added=datetime.datetime.now())
        data = {
            "Reported": True,
        }
        return Response(data)
