from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from django.contrib.auth.views import LoginView as BaseLoginView
from .forms import CreateRegisterForm, UpdateUserForm, UpdateUserProfileForm

# Class based functions
class LoginView(BaseLoginView):
    template_name = 'user/auth/login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.headers.get('HX-Request'):
            redirect_url = resolve_url(self.get_success_url())
            hx_response = HttpResponse()
            hx_response['HX-Redirect'] = redirect_url
            return hx_response
        
        return response

def index(request):
    return render(request, 'user/auth/page.html') 

def register(request):
    if request.method == 'POST':
        form = CreateRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            if request.headers.get("HX-Request"):
                response = HttpResponse()
                response['HX-Redirect'] = redirect('dashboard-home').url
                return response

            return redirect('dashboard-home')
    else:
        form = CreateRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'user/auth/register.html', context)

def reset(request):
    return render(request, 'user/auth/password_reset.html')

def profile(request):
    return render(request, 'user/profile.html')
 
def profile_update(request):
    if request.method == 'POST':
        userform = UpdateUserForm(request.POST, instance=request.user)
        profileform = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
    else: 
        userform = UpdateUserForm(instance=request.user)
        profileform = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'profileform': profileform
    }

    return render(request, 'user/profile_update_form.html', context)