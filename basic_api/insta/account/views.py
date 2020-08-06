from django.shortcuts import render, redirect

from blog.views import home_view
from account.forms import CreateUserForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

def register(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,"Account was created for" +user)
			return redirect('login_page')
	context = {'form':form}
	template = 'auth/register.html'
	return render(request,template, context)


def login_page(request):
	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,"username OR password is incorrect")
	return render(request,'auth/login.html')



@login_required(login_url='login_page')
def logoutUser(request):
	logout(request)
	return redirect('login_page')