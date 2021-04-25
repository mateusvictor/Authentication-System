from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import User
from .forms import *


def home(request):
	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'home.html')

def signup(request):
	return render(request, 'registration/signup.html')


class TeacherSignUpView(CreateView):
	model = User
	form_class = SignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)
							
	def form_valid(self, form):
		form.instance.is_teacher = True
		user = form.save()
		login(self.request, user)
		return redirect('home')


class StudentSignUpView(CreateView):
	model = User
	form_class = SignUpForm
	template_name = 'registration/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		form.instance.is_student = True
		user = form.save()
		login(self.request, user)
		return redirect('home')
