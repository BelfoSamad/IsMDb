from django.contrib.auth.admin import UserAdmin, GroupAdmin
from notifications.signals import notify

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import Member, MemberGroup
from admin.admin import admin_site


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Member
    list_display = ['email', 'username', ]

    def save_model(self, request, obj, form, change):
        user = request.user
        if obj.cant_comment:
            notify.send(user, recipient=obj, verb='Can\'t Comment Due To a Report')
        super().save_model(request, obj, form, change)


class CustomGroupAdmin(GroupAdmin):
    pass


admin_site.register(Member, CustomUserAdmin)
admin_site.register(MemberGroup, CustomGroupAdmin)
