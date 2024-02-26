from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

from user.forms import LoginUserForm, RegisteUserForm, ProfileEditMainForm


# Create your views here.

def home(request):
    return render(request, 'user/home.html')




def site_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('user:home_page')



    else:
        form = LoginUserForm()


    return render(request, 'user/login_form.html', {'form':form})


def site_logout(request):
    logout(request)
    return redirect('user:site_login')

def site_register(request):
    if request.method == 'POST':
        form = RegisteUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'user/register_done.html')
        else:
            return render(request, 'user/register_form.html', {'form': form})



    else:
        form = RegisteUserForm()
        return render(request, 'user/register_form.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = ProfileEditMainForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = ProfileEditMainForm()
        return render(request,'user/profile_page.html', {'form':form})


