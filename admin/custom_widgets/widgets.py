
from django import forms


class CustomSelectMultiple(forms.SelectMultiple):
    template_name = 'admin/custom_widgets/select.html'
    option_template_name = 'admin/custom_widgets/select_option.html'


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'admin/custom_widgets/checkbox_select.html'
    option_template_name = 'admin/custom_widgets/checkbox_option.html'

