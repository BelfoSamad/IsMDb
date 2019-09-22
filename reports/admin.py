from django.contrib import admin

# Register your models here.
from admin.admin import admin_site
from reports.models import ReportComment, ReportReview


class ReportAdmin(admin.ModelAdmin):
    exclude = ['date_added']


admin_site.register(ReportComment)
admin_site.register(ReportReview)
