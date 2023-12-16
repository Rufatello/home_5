from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, View, UpdateView
from django.urls import reverse_lazy, reverse
from users.forms import UserForm, UserUpdate
from users.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import get_user_model

import random

User = get_user_model()
class LogoutView(BaseLogoutView):
    pass


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:code')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_pass = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        new_user = form.save(commit=False)
        new_user.code = new_pass
        new_user.save()
        send_mail(
            subject='Подтверждение регистрации',
            message=f' Введите код: {new_user.code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return super().form_valid(form)


class CodeView(View):
    model = User
    template_name = 'users/code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        code = request.POST.get('code')
        user = User.objects.filter(code=code).first()

        if user is not None and user.code == code:
            user.is_active = True
            user.save()
            return redirect('users:login')


class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdate
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def new_password(request):
    new_pass = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    send_mail(
        subject='Новый пароль',
        message=f'Новый пароль {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)

    request.user.save()

    return redirect(reverse('users:login'))
