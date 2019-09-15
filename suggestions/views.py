from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from haystack.query import SearchQuerySet
from notifications.signals import notify
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from suggestions.models import Suggestion


class SuggestionsListView(ListView):
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
        user = self.request.user
        up_voted = False
        up_votes = 0
        if id != -1:
            obj = Suggestion.objects.get(id=id)
            if request.user is not obj.memberID:
                if user in obj.up_votes.all():
                    up_voted = False
                    obj.up_votes.remove(user)
                else:
                    up_voted = True
                    obj.up_votes.add(user)
                    notify.send(user, recipient=obj.memberID, verb='UpVoted Your Suggestion :', action_object=obj)
            up_votes = obj.up_votes.count()
        updated = True
        data = {
            "updated": updated,
            "up_voted": up_voted,
            "up_votes": up_votes
        }
        return Response(data)


def autocomplete(request, query):
    sqs = SearchQuerySet().autocomplete(content_auto=query)
    results = [result for result in sqs if (result.approved is False) and (result.memberId is request.user) and (
            request.user in result.up_votes.all())]
    template = loader.get_template('suggestions/suggestions_results.html')
    return HttpResponse(template.render({'suggestions': results}, request))
