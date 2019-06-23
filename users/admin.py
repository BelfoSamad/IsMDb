from admin.admin import admin_site

# Register your models here.
from users.models import Member

admin_site.register(Member)
