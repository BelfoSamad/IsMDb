from django.contrib import admin

# Register your models here.
from admin.admin import admin_site
from suggestions.models import Suggestion

admin_site.register(Suggestion)
