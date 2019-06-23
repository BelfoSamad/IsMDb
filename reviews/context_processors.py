from reviews.models import MovieReview


def add_variable_to_context(request):
    reviews = MovieReview.objects.all()

    return {
        'reviews': reviews
    }
