from django import forms

from .models import User


class UserRegisterForm(forms.Form):
	name = forms.CharField(max_length=100, required=True)
	matric_no = forms.CharField(max_length=100, required=True)
	password1 = forms.CharField(max_length=16, 
								min_length=6,
								widget=forms.PasswordInput, 
								required=True)
	password2 = forms.CharField(max_length=16, 
								min_length=6,
								widget=forms.PasswordInput, 
								required=True)


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password Don't match. Try again!")

		return password1



class UserLoginForm(forms.Form):
	matric_no = forms.CharField(max_length=100, required=True)
	password = forms.CharField(max_length=16, 
								min_length=6,
								widget=forms.PasswordInput, 
								required=True)