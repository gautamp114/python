from django.urls import path

from account import views

urlpatterns = [
	path('', views.register, name='register'),
	path('login_page/', views.login_page, name='login_page'),
	path('logoutUser/', views.logoutUser, name='logoutUser'),
]