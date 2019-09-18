from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from notifications.signals import notify

from suggestions.models import Suggestion


class SuggestionFilter(SimpleListFilter):
    title = 'Suggestions Approval'
    parameter_name = 'approval'

    def lookups(self, request, model_admin):
        return (
            ('Approved', 'All Approved'),
            ('Unapproved', 'All Unapproved'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Approved':
            return queryset.filter(approved=True)

        if self.value() == 'Unapproved':
            return queryset.filter(approved=False)


def approve_suggestion(modelAdmin, request, queryset):
    for suggestion in queryset:
        user = request.user
        print(user)
        print(suggestion.memberID)
        print(suggestion)
        notify.send(user, recipient=suggestion.memberID, verb='Suggestion Approved', action_object=suggestion)
        suggestion.approved = True
        suggestion.save()


approve_suggestion.short_description = 'Approve Suggestions'


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'memberID', 'description']
    exclude = ['up_votes']
    list_filter = [SuggestionFilter]
    actions = [approve_suggestion]


admin.site.register(Suggestion, SuggestionAdmin)
