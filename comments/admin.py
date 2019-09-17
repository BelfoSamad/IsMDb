from django.contrib import admin

from admin.admin import admin_site
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    exclude = ['date_added', 'likes', 'dislikes', 'alcohol', 'nudity', 'LGBTQ', 'sex', 'violence', '']


admin_site.register(Comment, CommentAdmin)
