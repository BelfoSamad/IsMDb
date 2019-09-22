from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews.models import MovieReview
from users.forms import UserForm, UserMemberInfoForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('reviews:reviews'))


def signup(request):
    print(request.POST)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('reviews:reviews'))
            else:
                return HttpResponse("Your account is inactive.")
        else:
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

