from haystack.forms import SearchForm
from django import forms
from haystack.forms import SearchForm


class DateRangeSearchForm(SearchForm):
    min_year = forms.IntegerField(required=False)
    max_year = forms.IntegerField(required=False)
    min_time = forms.IntegerField(required=False)
    max_time = forms.IntegerField(required=False)
    pub_from = forms.DateField(required=False)
    pub_to = forms.DateField(required=False)
    min_imdb = forms.IntegerField(required=False)
    max_imdb = forms.IntegerField(required=False)
    min_mpaa = forms.IntegerField(required=False)
    max_mpaa = forms.IntegerField(required=False)

    def search(self):

        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data.get('q'):
            return self.no_query_found()

        sqs = self.searchqueryset.filter(title__contains=self.cleaned_data['q'])

        # Check to see if an end_date was chosen.
        if self.cleaned_data['min_year']:
            sqs = sqs.filter(year__gte=self.cleaned_data['min_year'])

        if self.cleaned_data['max_year']:
            sqs = sqs.filter(year__lte=self.cleaned_data['max_year'])

        if self.cleaned_data['min_imdb']:
            sqs = sqs.filter(IMDB_rating__gte=self.cleaned_data['min_imdb'])

        if self.cleaned_data['max_imdb']:
            sqs = sqs.filter(IMDB_rating__lte=self.cleaned_data['max_imdb'])

        if self.cleaned_data['min_time']:
            sqs = sqs.filter(time__gte=self.cleaned_data['min_time'])

        if self.cleaned_data['max_time']:
            sqs = sqs.filter(time__lte=self.cleaned_data['max_time'])

        if self.cleaned_data['pub_from']:
            sqs = sqs.filter(release_date__gte=self.cleaned_data['pub_from'])

        if self.cleaned_data['pub_to']:
            sqs = sqs.filter(release_date__lte=self.cleaned_data['pub_to'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs
