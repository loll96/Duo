from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdate, ProfileUpdate
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html',{'title':'registration', 'form':form})

@login_required 
def profile(request, username):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data['username']
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile', username=username)
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)
    return render(request, 'users/profile.html',{
        'u_form':u_form,
        'p_form':p_form,
        'user_name':User.objects.get(username=username)
    })