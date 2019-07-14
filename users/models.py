import datetime
from django.contrib.auth.models import User, AbstractUser, Group
from django.db import models
from django_countries.fields import CountryField


class Member(AbstractUser):
    models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = CountryField(default='US', null=False)
    birthday_date = models.DateField(default=datetime.date.today)
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    honor_points = models.IntegerField(default=0)
    watchlist = models.ManyToManyField('reviews.MovieReview', blank=True, related_name='watch_list')

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

class MemberGroup(Group):
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
