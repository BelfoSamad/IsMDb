from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    exclude = ['alcohol', 'nudity', 'LGBTQ', 'sex', 'violence', 'language', 'likes', 'dislikes']
    pass


admin.site.register(Comment, CommentAdmin)
