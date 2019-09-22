from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from admin.forms import UserUpdateForm
from reviews.models import MovieReview
from suggestions.models import Suggestion
from users.models import Member, MemberGroup


@user_passes_test(lambda u: u.is_superuser)
def history(request, admin_site_instance):
    # history = MovieReview.history.all()
    members_history = Member.history.all()
    MemberGroup_history = MemberGroup.history.all()
    Suggestion_history = Suggestion.history.all()
    MovieReview_history = MovieReview.history.all()
    list_of_querysets = [members_history,MemberGroup_history,Suggestion_history,MovieReview_history]
    full_history = []
    for qs in list_of_querysets :
        for history_object in qs :
            full_history.append(history_object)

    full_history.sort(reverse=True, key=lambda x: x.history_date)

    context = {
        **admin_site_instance.each_context(request),
        'history' : full_history,
    }
    return render(request, 'admin/history.html', context)


@user_passes_test(lambda u: u.is_superuser)
def account(request, admin_site_instance):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('admin:account')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        **admin_site_instance.each_context(request),
        'u_form': u_form,
    }
    return render(request, 'admin/account.html', context)

