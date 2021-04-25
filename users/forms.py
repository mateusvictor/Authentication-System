from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


class SignUpForm(UserCreationForm):
	email = forms.EmailField()

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'email', 'password1', 'password2']
