from django.contrib import admin

# Register your models here.
from users.models import Member

admin.site.register(Member)
