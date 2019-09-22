from django.contrib import admin
from django.db import models
from simple_history.admin import SimpleHistoryAdmin

from admin.admin import admin_site
from admin.widgets import MyAdminSplitDateTime, AdminTimeWidget, AdminDateWidget
from reviews.models import Actor, Director, Writer, MovieReview


class MovieReviewAdmin(SimpleHistoryAdmin):
    exclude = ['slug', 'pub_date', 'likes']
    change_list_template = 'admin/reviews/change_list.html'
    change_form_template = 'admin/reviews/change_form.html'
    list_per_page = 12
    formfield_overrides = {
        models.DateTimeField : { 'widget' : MyAdminSplitDateTime},
        models.TimeField: { 'widget' : AdminTimeWidget},
        models.DateField: { 'widget' : AdminDateWidget},
    }


admin_site.register(Actor)
admin_site.register(Director)
admin_site.register(Writer)
admin_site.register(MovieReview, MovieReviewAdmin)
