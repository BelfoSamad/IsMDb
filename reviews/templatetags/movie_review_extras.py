from django import template

register = template.Library()


@register.filter('duration_format')
def duration_format(value):
    value = int(value)
    h = 'h'
    m = 'min'
    hours = int(value / 60)
    minutes = value % 60

    return '%s%s %s%s' % (hours, h, minutes, m)


@register.filter('genre_text')
def genre_text(value):
    value = int(value)
    genre_choices = ((1, 'Action'),
                     (2, 'Adventure'),
                     (3, 'Animation'),
                     (4, 'Comedy'),
                     (5, 'Crime'),
                     (6, 'Drama'),
                     (7, 'Fantasy'),
                     (8, 'Historical'),
                     (9, 'Horror'),
                     (10, 'Mystery'),
                     (11, 'Political'),
                     (12, 'Romance'),
                     (13, 'Satire'),
                     (14, 'Sci-Fi'))
    choices = dict(genre_choices)
    return choices[value]
