from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _

from users.models import Member


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['avatar', 'username', 'email']

