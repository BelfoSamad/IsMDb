from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from admin.forms import UserUpdateForm



# @login_required
@user_passes_test(lambda u: u.is_superuser)
def account(request, admin_instance):
    request.current_app = admin_instance.name
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('admin:account')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        **admin_instance.each_context(request),
        'u_form': u_form
    }
    return render(request, 'admin/account.html', context)


