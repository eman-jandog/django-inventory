from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='login-page'),
    path('login/', views.LoginView.as_view(template_name='user/auth/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('register/', views.register, name='user-register'),
    path('profile/', views.profile, name='user-profile'),
    path('update_profile/', views.profile_update, name='user-update-profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/auth/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/auth/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='user/auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/auth/password_reset_complete.html'), name='password_reset_complete')
]