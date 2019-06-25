from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    exclude = ['date_added', 'likes', 'dislikes', 'alcohol', 'nudity', 'LGBTQ', 'sex', 'violence', '']


admin.site.register(Comment, CommentAdmin)
