
from django import template

register = template.Library()

@register.filter
def get_admin_edit_url(obj):
    # return obj.__class__.__name__
    app_label = obj._meta.app_label
    model_name = obj._meta.model_name.replace('historical','')
    return f"/admin/{app_label}/{model_name}/{obj.id}/change"

@register.filter
def get_admin_history_url(obj):
    # return obj.__class__.__name__
    app_label = obj._meta.app_label
    model_name = obj._meta.model_name.replace('historical','')
    return f"/admin/{app_label}/{model_name}/{obj.id}/history/{obj.history_id}"


@register.filter
def my_show(obj):
    all_attr = dir(obj)
    print(all_attr)
    return obj