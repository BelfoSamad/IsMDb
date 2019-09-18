from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    # TODO: exclude likes and dislikes
    # exclude = ['alcohol', 'nudity', 'LGBTQ', 'sex', 'violence', 'language']
    pass


admin.site.register(Comment, CommentAdmin)
