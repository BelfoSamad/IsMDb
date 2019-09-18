from django.contrib import admin
from reviews.models import Actor, Director, Writer, MovieReview


class MovieReviewAdmin(admin.ModelAdmin):
    #TODO: exclude likes
    exclude = ['slug', 'pub_date']


admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(MovieReview, MovieReviewAdmin)
