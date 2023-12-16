from django.urls import path
from users.views import LogoutView, LoginView, RegisterView, CodeView, UserUpdate, new_password
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('code/', CodeView.as_view(), name='code'),
    path('profile/', UserUpdate.as_view(), name='profile'),
    path('profile/newpassword', new_password, name='new_password'),
]
