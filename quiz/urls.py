from django.urls import path
from . import views


urlpatterns = [
	path('', views.UserLoginView.as_view(), name="login"),
	path('logout/', views.UserLogoutView.as_view(), name="logout"),
	path('register/', views.UserRegisterView.as_view(), name="register"),
	path('quiz_page/', views.QiuzView.as_view(), name="quiz-page"),
]