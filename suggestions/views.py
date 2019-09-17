from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from haystack.query import SearchQuerySet
from notifications.signals import notify
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from suggestions.models import Suggestion


class SuggestionsListView(ListView):
    template_name = 'suggestions/suggestions.html'
    model = Suggestion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        my_suggestions = Suggestion.objects.filter(memberID=current_user, approved=True)
        other_suggestions = Suggestion.objects.exclude(memberID=current_user, approved=False)
        if current_user.is_authenticated:
            context['my_suggestions'] = my_suggestions
        else:
            context['my_suggestions'] = []

        context['other_suggestions'] = other_suggestions
        # Notification:
        if self.request.user.is_authenticated:
            context['notifications'] = current_user.notifications.unread()
        return context


class SuggestionCreateView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        title = request.GET.get('title', None)
        description = request.GET.get('description', None)
        Suggestion.objects.create(title=title, description=description, memberID=user)
        data = {
            "added": True,
        }
        return Response(data)


class SuggestionDelete(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        deleted = False
        if id != -1:
            Suggestion.objects.filter(id=id).delete()
            deleted = True
        data = {
            "deleted": deleted,
        }
        return Response(data)


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
                    notify.send(user, recipient=obj.memberID, verb='Suggestion Upvoted', action_object=obj)
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
    results = []
    for result in sqs:
        if (result.object.approved is False) and (request.user not in result.object.up_votes) and (
                result.object.memberID is not request.user):
            results.append(result)
    template = loader.get_template('suggestions/suggestions_results.html')
    return HttpResponse(template.render({'suggestions': results}, request))
