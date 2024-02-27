from django import forms
from django.contrib.auth import get_user_model



class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())





class RegisteUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Surname")

    class Meta:
        model = get_user_model()
        fields = ['img','username', 'email', 'password', 'password2', 'first_name', 'last_name',]

    def clean_username(self):
        username = self.cleaned_data['username']
        user_model = get_user_model()
        if user_model.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой login уже существует!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user_model = get_user_model()
        if user_model.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password2']



class ProfileEditMainForm(forms.ModelForm):
    username = forms.CharField(label="Логин", disabled=True)

    class Meta:
        model = get_user_model()
        fields = [ 'img', 'username', 'email', 'first_name', 'last_name']





