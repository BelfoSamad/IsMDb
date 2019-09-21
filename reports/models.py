import datetime

from django.db import models

# Create your models here.
from comments.models import Comment
from reviews.models import MovieReview
from users.models import Member


class ReportComment(models.Model):
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    commentID = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)
    message = models.CharField(max_length=255, blank=True)
    date_added = models.DateField(default=datetime.date.today)


class ReportReview(models.Model):
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    reviewID = models.ForeignKey(MovieReview, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)
    message = models.CharField(max_length=255, blank=True)
    date_added = models.DateField(default=datetime.date.today)
