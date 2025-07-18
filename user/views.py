from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateRegisterForm

# Create your views here.
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

    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')