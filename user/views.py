from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from user.forms import LoginUserForm, RegisteUserForm, ProfileEditMainForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request, 'user/home.html')




def site_login(request):
    if request.user.username:
        return redirect('user:profile')

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
        form = RegisteUserForm(request.POST, request.FILES)
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


class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user/profile_page.html'
    form_class = ProfileEditMainForm
    success_url = 'user:profile'


    def get_success_url(self):
        return reverse_lazy('user:profile', args=[self.request.user.pk])

    def get_object(self, queryset=None):
        return self.request.user




