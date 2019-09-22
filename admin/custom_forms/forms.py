from multiselectfield.forms.fields import MultiSelectFormField
from django import forms

from admin.custom_widgets.widgets import CustomCheckboxSelectMultiple


class CustomMultiSelectFormField(MultiSelectFormField):
    widget = CustomCheckboxSelectMultiple
