from admin.admin import admin_site

# Register your models here.
from reviews.models import MovieReview, Actor, Director, Producer, Writer

admin_site.register(Actor)
admin_site.register(Director)
admin_site.register(Producer)
admin_site.register(Writer)
admin_site.register(MovieReview)
