from django import template
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from admin.templatetags.admin_list import DOT

register = template.Library()
@register.simple_tag
def paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == DOT:
        return '… '
    elif i == cl.page_num:
        return format_html('<li class="active"><a>{}</a></li> ', i + 1)
    else:
        return format_html(
            '<li class="waves-effect"><a href="{}"{}>{}</a></li> ',
            cl.get_query_string({PAGE_VAR: i}),
            mark_safe(' class="waves-effect"' if i == cl.paginator.num_pages - 1 else ''),
            i + 1,
        )

