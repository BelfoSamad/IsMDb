from django import template

register = template.Library()


@register.filter('duration_format')
def duration_format(value):
    value = int(value)
    h = 'h'
    m = 'm'
    hours = int(value / 60)
    minutes = value % 60

    return '%s%s %s%s' % (hours, h, minutes, m)
