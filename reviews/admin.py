from admin.admin import admin_site
# from django.contrib import admin
from admin.admin import MyModelAdmin
from reviews.models import Actor, Director, Producer, Writer, MovieReview


class MovieReviewAdmin(MyModelAdmin):
    exclude = ['slug', 'pub_date', 'likes']


admin_site.register(Actor)
admin_site.register(Director)
admin_site.register(Producer)
admin_site.register(Writer)
admin_site.register(MovieReview, MovieReviewAdmin)
