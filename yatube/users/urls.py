from django.contrib.auth.views import *
from django.urls import path, reverse_lazy

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    # Смена пароля
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html', #<form method="post" action="{% url 'users:password_change' %}">
            success_url=reverse_lazy('users:password_change_done')),
        name='password_change'
    ),
    # Сообщение об успешном изменении пароля
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    # Восстановление пароля
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/password_reset_form.html',
            success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'
    ),
    # Сообщение об отправке ссылки для восстановления пароля
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'),

        name='password_reset_done'
    ),
    # Вход по ссылке для восстановления пароля 'users:password_reset_confirm', kwargs={'uidb64': 'x', 'token': 'x'}
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url=reverse_lazy('users:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    # Сообщение об успешном восстановлении пароля
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
