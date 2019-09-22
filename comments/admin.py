from django.contrib import admin

from admin.admin import admin_site
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    exclude = ['alcohol', 'nudity', 'LGBTQ', 'sex', 'violence', 'language', 'likes', 'dislikes']
    pass


admin_site.register(Comment, CommentAdmin)
