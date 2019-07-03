from django import forms


class CommentForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Comment Title'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Comment...'}))
