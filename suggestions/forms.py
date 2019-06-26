from django import forms
from suggestions.models import Suggestion


class SuggestionModelForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = [
            'title',
            'description',
        ]
