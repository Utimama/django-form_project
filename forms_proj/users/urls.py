from django.urls import path
from .views import signup_view, logout_confirm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns=[
    path('signup/', signup_view, name="user-signup"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name='user-login'),
    path('logout-confirm/', logout_confirm, name="logout-confirm"),
    path("logout/", LogoutView.as_view(), name="logout-user"),
    path('reset_password/', PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path('password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="accounts/reset.html"), name="password_reset_confirm"),
    path('reset/complete/', PasswordResetCompleteView.as_view(template_name="accounts/complete.html"), name="password_reset_complete")    
]