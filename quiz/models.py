from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	matric_no = models.CharField(max_length=100, null=True, blank=True, unique=True)
	email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return self.matric_no




