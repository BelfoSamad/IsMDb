from django import forms
from users.models import Member
from django.contrib.auth.models import User


# Create your views here.


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), max_length=40)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class UserMemberInfoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('birthday_date', 'country')
