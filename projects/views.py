from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth,messages
from django.contrib.auth.models import User
from .models import Project,Blog
from django.views.generic.detail import DetailView


def home(request):
	return render(request, 'projects/home.html', {})

def contact(request):
	return render(request, 'projects/contact.html', {})
def about(request):
	return render(request, 'projects/about.html', {})

def portfolio(request):
	projects = Project.objects.all
	return render(request, 'projects/portfolio.html', {'projects': projects})

def blog(request):
	return render(request, 'projects/blog.html', {})


def signup_user(request):
	if request.method == 'POST':
		if request.POST['password1']==request.POST['password2']:
			username = request.POST['username']
			password = request.POST['password1']
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'projects/signup.html', {'error':'username is already taken'})
			except User.DoesNotExist:
			    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
			    auth.login(request, user)
			    return render(request, 'projects/home.html', {'error':'you successfully signup!!'})		
		else:
			return render(request, 'projects/signup.html', {'error':'password doesnt matched !!'})
	else:
		return render(request, 'projects/signup.html', {})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return render(request, 'projects/home.html', {'error':'successfully logged in'})
		else:
			return render(request, 'projects/login.html', {'error': 'Incorrect username or password !!'})
	else:
		return render(request, 'projects/login.html', {})

def logout_user(request):
	auth.logout(request)
	# messages.success(request, ('you successfully logout'))
	return render(request, 'projects/home.html', {'error':'you successfully logged out!!'})




