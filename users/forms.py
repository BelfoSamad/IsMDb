from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import Member
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Member
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ('username', 'email')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), max_length=40)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')


class UserMemberInfoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('birthday_date', 'country')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Member
        fields = ['username','email','avatar']

