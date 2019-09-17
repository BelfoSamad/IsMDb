from django.contrib import admin


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    exclude = ['date_added']
