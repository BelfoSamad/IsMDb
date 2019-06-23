from django.contrib import admin

# Register your models here.
from admin.admin import admin_site
from comments.models import Comment

admin_site.register(Comment)
