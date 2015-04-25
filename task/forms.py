from django.forms import Form
from django.forms import CharField
from django.forms import EmailField
from django.forms import PasswordInput

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserCreateForm(Form):
    user = CharField()
    name = CharField(required=False)
    email = EmailField(required=False)
    password = CharField(widget=PasswordInput)
    password_confirm = CharField(widget=PasswordInput)

    def save(self):
        params = {
            'username': self.cleaned_data['user'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password'],
        }
        if self.cleaned_data['name']:
            params['first_name'] = self.cleaned_data['name']
        User.objects.created_user(**params)

    def clean_password_confirm(self, password):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password_confirm']

        if password1 != password2:
            raise ValidationError("As senhas devem ser iguais.")
        return password
