from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from suggestions.models import Suggestion


class SuggestionsListView(ListView):
    print('in')
    template_name = 'suggestions/suggestions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        my_suggestions = Suggestion.objects.filter(memberID=current_user)
        other_suggestions = Suggestion.objects.exclude(memberID=current_user)
        context['my_suggestions'] = my_suggestions
        context['other_suggestions'] = other_suggestions
        return context


class SuggestionCreateView(CreateView):
    template_name = 'suggestions/add_suggestion.html'
    model = Suggestion
    fields = ('title', 'description')
    success_url = reverse_lazy('suggestions:suggestions')

    def form_valid(self, form):
        form.instance.memberID = self.request.user
        return super(SuggestionCreateView, self).form_valid(form)


class SuggestionUpVote(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        print(id)
        liked = False
        if id != -1:
            obj = Suggestion.objects.get(id=id)
            if user in obj.up_votes.all():
                liked = False
                obj.up_votes.remove(user)
            else:
                liked = True
                obj.up_votes.add(user)
        updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)

