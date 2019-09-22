from django.forms import MultipleChoiceField
from django.utils.text import capfirst
from multiselectfield.db.fields import MultiSelectField

from admin.custom_forms.forms import CustomMultiSelectFormField
from admin.custom_widgets.widgets import CustomSelectMultiple


class CustomMultipleChoiceField(MultipleChoiceField):
    widget = CustomSelectMultiple


class CustomMultiSelectField(MultiSelectField):

    def formfield(self, **kwargs):
        defaults = {'required': not self.blank,
                    'label': capfirst(self.verbose_name),
                    'help_text': self.help_text,
                    'choices': self.choices,
                    'max_length': self.max_length,
                    'max_choices': self.max_choices}
        if self.has_default():
            defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        return CustomMultiSelectFormField(**defaults)



