from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from users.forms import UserForm
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
class LogoutView(BaseLogoutView):
    pass



class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('catalog:home')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='салам алейкум ержан',
            message=f'перейдите по этой ссылке: http://127.0.0.1:8000/users/code/,  введите код: {new_user.ver_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return super().form_valid(form)

# class CodeCreateView(CreateView):
#     model = User
#     fields = ('ver_code',)
#     template_name = 'users/code.html'
#     success_url = reverse_lazy('catalog:home')

from django.http import HttpResponse


class CodeView(View):
    template_name = 'users/code.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        ver_code = request.POST.get('ver_code')
        user_code = User.objects.filter(ver_code=ver_code).first()

        if user_code is not None and user_code.ver_code == ver_code:
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')

        context = {'error': 'Invalid verification code.'}
        return render(request, self.template_name, context)