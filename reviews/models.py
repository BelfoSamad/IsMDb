import datetime

from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from languages.fields import LanguageField
from multiselectfield import MultiSelectField
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


class Producer(Staff):
    pass


class Writer(Staff):
    pass


class MovieReview(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    cover = models.ImageField(default='default_cast.png', upload_to="gallery")
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
    genre = MultiSelectField(choices=GENRE_CHOICES, null=False)
    time = models.IntegerField(blank=True, null=False, default=0)
    release_date = models.DateField(default=datetime.date.today)
    description = models.TextField(max_length=255, blank=True, null=False)
    country = CountryField(default='US', null=False)
    movie_language = LanguageField(default='En', null=False)
    IMDB_rating = models.FloatField(max_length=255, blank=True, null=True)
    date_created = models.DateField(default=datetime.date.today)
    alcohol = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    nudity = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    LGBTQ = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    sex = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    language = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    violence = FloatRangeField(min_value=0.0, max_value=5.0, default=0.0)
    cast_actor = models.ManyToManyField(Actor)
    cast_producer = models.ManyToManyField(Producer)
    cast_writer = models.ManyToManyField(Writer)
    cast_director = models.ManyToManyField(Director)

    def get_absolute_url(self):
        return "/reviews/?id=" % self.id

    def __str__(self):
        return self.title


