
from django import forms
from django.forms import TextInput
from django.utils.translation import gettext as _


class AdminDateWidget(forms.DateInput):
    class Media:
        js = [
            'custom/js/panel.js',
            'admin/js/admin/DateTimeShortcuts.js',
            'admin/js/calendar.js',
        ]

    def __init__(self, attrs=None, format=None):
        attrs = {'class': 'vDateField datepicker', 'size': '10', **(attrs or {})}
        super().__init__(attrs=attrs, format=format)


class AdminTimeWidget(forms.TimeInput):
    class Media:
        js = [
            'custom/js/panel.js',
            'admin/js/admin/DateTimeShortcuts.js',
            'admin/js/calendar.js',
        ]

    def __init__(self, attrs=None, format=None):
        attrs = {'class': 'vTimeField timepicker', 'size': '8', **(attrs or {})}
        super().__init__(attrs=attrs, format=format)


class MyAdminSplitDateTime(forms.SplitDateTimeWidget):
    """
    A SplitDateTime Widget that has some admin-specific styling.
    """
    template_name = 'admin/widgets/split_datetime.html'

    def __init__(self, attrs=None):
        widgets = [AdminDateWidget, AdminTimeWidget]
        # Note that we're calling MultiWidget, not SplitDateTimeWidget, because
        # we want to define widgets.
        forms.MultiWidget.__init__(self, widgets, attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['date_label'] = _('Date:')
        context['time_label'] = _('Time:')
        return context






