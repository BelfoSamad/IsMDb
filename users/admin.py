from django.contrib.auth.admin import UserAdmin, GroupAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import Member, MemberGroup
from admin.admin import admin_site


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Member
    list_display = ['email', 'username', ]


class CustomGroupAdmin(GroupAdmin):
    pass


admin_site.register(Member, CustomUserAdmin)
admin_site.register(MemberGroup, CustomGroupAdmin)
