from django.contrib import admin
from suggestions.models import Suggestion


class SuggestionAdmin(admin.ModelAdmin):
    exclude = ['up_votes']


admin.site.register(Suggestion, SuggestionAdmin)
