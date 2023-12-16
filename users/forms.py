from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'avatar')


class UserUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserUpdate, self).__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
