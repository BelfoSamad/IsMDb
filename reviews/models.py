import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import SlugField
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django_countries.fields import CountryField
from languages.fields import LanguageField
from multiselectfield import MultiSelectField
from notifications.signals import notify

from admin.custom_fields.fields import CustomMultiSelectField
from suggestions.models import Suggestion
from users.models import Member


class FloatRangeField(models.FloatField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.FloatField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(FloatRangeField, self).formfield(**defaults)


class Staff(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    profile_picture_url = models.ImageField(default='default_cast.png', upload_to='gallery')

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Actor(Staff):
    pass


class Director(Staff):
    pass


class Writer(Staff):
    pass


class MovieReview(models.Model):
    published = models.BooleanField(default=True)
    title = models.CharField(max_length=255, blank=True, null=False)
    slug = SlugField(max_length=255)
    poster = models.ImageField(default='default_poster.png', upload_to="gallery")
    cover = models.ImageField(default='default_cover.png', upload_to="gallery")
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    GENRE_CHOICES = ((1, 'Action'),
                     (2, 'Adventure'),
                     (3, 'Animation'),
                     (4, 'Comedy'),
                     (5, 'Crime'),
                     (6, 'Drama'),
                     (7, 'Fantasy'),
                     (8, 'Historical'),
                     (9, 'Horror'),
                     (10, 'Mystery'),
                     (11, 'Political'),
                     (12, 'Romance'),
                     (13, 'Satire'),
                     (14, 'Sci-Fi'))
    genre = CustomMultiSelectField(choices=GENRE_CHOICES, null=False)
    time = models.IntegerField(blank=True, null=False, default=0)
    release_date = models.DateField(default=datetime.date.today)
    description = models.TextField(max_length=255, blank=True, null=False)
    review = models.TextField(max_length=255, blank=True, null=True)
    tags = models.TextField(blank=True)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.SET_NULL, null=True, blank=True)
    country = CountryField(default='US', null=False)
    movie_language = LanguageField(default='En', null=False)
    IMDB_rating = models.FloatField(max_length=255, blank=True, null=True)
    pub_date = models.DateField(default=datetime.datetime.now())
    alcohol = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    nudity = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    LGBTQ = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    sex = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    language = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    violence = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    cast_actor = models.ManyToManyField(Actor)
    cast_writer = models.ManyToManyField(Writer)
    cast_director = models.ManyToManyField(Director)
    trailer = models.CharField(max_length=255, blank=True)
    likes = models.ManyToManyField(Member, blank=True, related_name='review_likes')

    def get_absolute_url(self):
        return reverse('reviews:review', kwargs={'slug': self.slug})

    def split_tags(self):
        return self.tags.split(',')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(MovieReview, self).save(*args, **kwargs)
        suggestion = self.suggestion
        if suggestion is not None:
            for user in suggestion.up_votes.all():
                notify.send(user, recipient=user,
                            verb='Suggestion Added',
                            action_object=self)
            suggestion.delete()


def pre_save_movie_receiver(sender, instance, *args, **kwargs):
    instance.slug = "%s-%s" % (slugify(instance.title), instance.year)


pre_save.connect(pre_save_movie_receiver, sender=MovieReview)
