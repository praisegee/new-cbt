from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import generic

from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(generic.View):

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'register.html', context)


	def post(self, request, *args, **kwargs):

		context = {}

		form = UserRegisterForm(request.POST or None)

		if form.is_valid():
			name = form.cleaned_data.get('name').title()
			matric_no = form.cleaned_data.get('matric_no')
			password1 = form.cleaned_data.get('password1')
			
			user = User.objects.create_user(username=matric_no)
			user.set_password(password1)
			user.save()
			messages.success(request, f"Account created for {name}!")
			return redirect('login')

		print(form.errors)
		messages.error(request, "Invalid details!")
		return render(request, 'register.html', context)




class UserLoginView(generic.View):

	def get(self, request, *args, **kwargs):
		context = {}
		return render(request, 'login.html', context)


	def post(self, request, *args, **kwargs):

		context = {}

		form = UserLoginForm(request.POST or None)

		if form.is_valid():	
			matric_no = form.cleaned_data.get('matric_no')
			password = form.cleaned_data.get('password')

			user = authenticate(request, username=matric_no, password=password)

			if user is not None:
				login(request, user)
				return redirect('quiz-page')
		print(form.errors)
		messages.error(request, "Invalid details!")
		return render(request, 'login.html', context)



class UserLogoutView(generic.View):

	def get(self, request, *args, **kwargs):

		if request.user.is_authenticated:
			logout(request)
			return redirect('login')

		return render(request, 'quiz-page.html', context)



class QiuzView(generic.View):

	def get(self, request, *args, **kwargs):

		context = {}

		return render(request, 'quiz-page.html', context)






