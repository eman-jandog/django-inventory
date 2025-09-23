from django.shortcuts import render, redirect
from django.contrib.auth import views
from .forms import CreateRegisterForm, UpdateUserForm, UpdateUserProfileForm

def index(request):
    return render(request, 'user/auth/base.html') 

def register(request):
    if request.method == 'POST':
        form = CreateRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-home')
    else:
        form = CreateRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'user/auth/register.html', context)

def reset(request):
    return render(request, 'user/auth/reset.html')

def profile(request):
    return render(request, 'user/profile.html')
 
def profile_update(request):
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST, instance=request.user)
        profileform = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            onEdit = False
    else: 
        userform = UpdateUserForm(instance=request.user)
        profileform = UpdateUserProfileForm(instance=request.user.profile)
        onEdit = True

    context = {
        'userform': userform,
        'profileform': profileform,
        'onEdit': onEdit
    }

    return render(request, 'user/profile_update_form.html', context)