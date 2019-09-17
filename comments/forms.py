from django import forms


class CommentForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Comment Title'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'placeholder': 'Comment...'}))
    alcohol = forms.FloatField(label='Alcohol', max_value=5, min_value=0)
    language = forms.FloatField(label='Language', max_value=5, min_value=0)
    lgbtq = forms.FloatField(label='LGBTQ', max_value=5, min_value=0)
    nudity = forms.FloatField(label='Nudity', max_value=5, min_value=0)
    sex = forms.FloatField(label='Sex', max_value=5, min_value=0)
    violence = forms.FloatField(label='Violence', max_value=5, min_value=0)
