import datetime
from haystack import indexes
from reviews.models import MovieReview


class MovieReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    year = indexes.IntegerField(model_attr='year')
    time = indexes.IntegerField(model_attr='time')
    release_date = indexes.DateField(model_attr='release_date')
    IMDB_rating = indexes.IntegerField(model_attr='IMDB_rating')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return MovieReview

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
