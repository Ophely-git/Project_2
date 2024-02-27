# from django.contrib import admin
from django.urls import path, include, reverse_lazy
import user.views as views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('profile/', views.ProfileEdit.as_view(), name='profile'),

    path('login/', views.site_login, name='site_login'),
    path('logout/', views.site_logout, name='site_logout'),
    path('register/', views.site_register, name='site_register'),

    path('password-change/', PasswordChangeView.as_view(success_url=reverse_lazy('user:password_change_done')), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"), name='password_change_done'),

    path('password-reset/', PasswordResetView.as_view(
        email_template_name="user/password_reset_email.html",
        success_url=reverse_lazy("user:password_reset_done"),
        template_name="user/password_reset_form.html"
    ),name='password_reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name = "user/password_reset_done.html",
    ),name='password_reset_done'),

    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy("user:password_reset_complete"),
        template_name = "user/password_reset_confirm.html",
    ),name='password_reset_confirm'),

    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name = "user/password_reset_complete.html",
    ),name='password_reset_complete'),
]
