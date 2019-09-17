from haystack import indexes

from reviews.models import MovieReview
from suggestions.models import Suggestion


class MovieReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    year = indexes.IntegerField(model_attr='year')
    description = indexes.CharField(model_attr='description')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return MovieReview

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class SuggestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Suggestion

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
