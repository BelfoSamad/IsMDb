from django.contrib import admin

# Register your models here.
from reports.models import ReportComment, ReportReview


class ReportAdmin(admin.ModelAdmin):
    exclude = ['date_added']


admin.site.register(ReportComment)
admin.site.register(ReportReview)
