from django.db import models
from users.models import Member


class Suggestion(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    description = models.CharField(max_length=255, blank=True, null=False)
    up_votes = models.ManyToManyField(Member, blank=True, related_name='up_vote')
    memberID = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Suggestion, self).save(*args, **kwargs)
        self.up_votes.add(self.memberID)

    def __str__(self):
        return self.title
