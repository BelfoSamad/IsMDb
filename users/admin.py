from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib import admin
from notifications.signals import notify
from simple_history.admin import SimpleHistoryAdmin

from admin.admin import admin_site
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import Member, MemberGroup


class CustomUserAdmin(UserAdmin,SimpleHistoryAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Member
    list_display = ['username', 'email', 'avatar', 'country', 'birthday_date', 'gender', ]

    def save_model(self, request, obj, form, change):
        user = request.user
        if obj.cant_comment:
            notify.send(user, recipient=obj, verb='Comment Disabled')
        super().save_model(request, obj, form, change)


class CustomGroupAdmin(GroupAdmin,SimpleHistoryAdmin):
    pass


admin_site.register(Member, CustomUserAdmin)
admin_site.register(MemberGroup, CustomGroupAdmin)
