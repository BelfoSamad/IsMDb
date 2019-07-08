from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews.models import MovieReview
from users.forms import UserForm, UserMemberInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'users/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserMemberInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserMemberInfoForm()
    return render(request, 'users/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'users/login.html', {})


class BookmarkReview(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        # id = self.kwargs.get("id")
        user = self.request.user
        bookmarked = False
        if id != -1:
            obj = MovieReview.objects.get(id=id)
            if obj in user.watchlist.all():
                bookmarked = False
                user.watchlist.remove(obj)
            else:
                bookmarked = True
                user.watchlist.add(obj)
        updated = True
        data = {
            "updated": updated,
            "bookmarked": bookmarked
        }
        return Response(data)


class WatchListView(ListView):
    template_name = 'users/bookmarks.html'
    context_object_name = 'reviews_list'

    def get_queryset(self):
        queryset = self.request.user.watchlist.all()
        return queryset
