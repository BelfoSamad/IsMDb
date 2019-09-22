from django.db import models
from notifications.signals import notify

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
        if self.approved is True:
            notify.send(self.memberID, recipient=self.memberID, verb='Suggestion Approved', action_object=self)
            self.memberID.honor_points = self.memberID.honor_points + 1
            self.memberID.save()
            notify.send(self.memberID, recipient=self.memberID, verb='Honor Points Added')

    def __str__(self):
        return self.title
