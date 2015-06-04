from django.core.exceptions import ValidationError
from django.forms.fields import Field
from django.forms.widgets import Widget
from django.forms.utils import flatatt

from django.utils.html import format_html, mark_safe
from django.utils.encoding import force_text
from django.utils.translation import gettext_lazy as _


class EnumSelect(Widget):
    allow_multiple_selected = False

    def __init__(self, enum, attrs=None):
        super(EnumSelect, self).__init__(attrs)
        self.enum = enum

    def render(self, name, value, attrs=None):

        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{}>', flatatt(final_attrs))]
        options = self.render_options([value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe('\n'.join(output))

    def render_options(self, selected_choices):
        selected_choices = set(map(force_text, selected_choices))
        options = []
        if not self.is_required:
            options.append(self.render_option(selected_choices, None))
        options.extend(self.render_option(selected_choices, value)
                       for value in self.enum)
        return '\n'.join(options)

    def render_option(self, selected_choices, option):
        if option is None:
            option_value = ''
            option_label = '---------'
        else:
            option_value = option.name
            option_label = force_text(option)

        attrs = {'value': option_value}
        if option_value in selected_choices:
            attrs['selected'] = True
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        return format_html('<option{}>{}</option>',
                           flatatt(attrs),
                           option_label)


class EnumField(Field):
    widget = EnumSelect
    empty_value = None

    default_error_messages = {
        'invalid_choice': _('Select a valid choice. %(value)s is not one of the available choices.'),
    }

    def __init__(self, enum, *, widget=None, **kwargs):
        self.enum = enum
        if widget is None:
            widget = self.widget
        if isinstance(widget, type):
            widget = widget(enum)
        super().__init__(widget=widget, **kwargs)

    def prepare_value(self, value):
        if value is None:
            return None
        return value.name

    def to_python(self, value):
        if value == self.empty_value or value in self.empty_values:
            return self.empty_value

        try:
            return self.enum[value]
        except KeyError:
            raise ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice',
                params={'value': value},
            )
