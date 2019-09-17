import datetime

from django.db import models

from reviews.models import MovieReview
from users.models import Member


class FloatRangeField(models.FloatField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.FloatField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(FloatRangeField, self).formfield(**defaults)


class Comment(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    reviewID = models.ForeignKey(MovieReview, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    content = models.TextField(blank=True, null=False)
    likes = models.ManyToManyField(Member, related_name='likes')
    dislikes = models.ManyToManyField(Member, related_name='dislikes')
    alcohol = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    nudity = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    LGBTQ = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    sex = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    language = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    violence = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)

    def __str__(self):
        return self.title
