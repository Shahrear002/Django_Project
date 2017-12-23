from django.shortcuts import render, HttpResponse, redirect
from .forms import signuppf
#from django.urls import reverse
#from django.contrib.auth.form UserCreationForm  

def index(request):
	return render(request, 'personal/firstpage.html')

def signupp(request):
	if request.method == 'POST':
		form = signuppf(request.POST)
		if form.is_valid():
			pass
	else:
		form = signuppf()
	return render(request, 'personal/signupp.html', {'form': form})

def signupd(request):
	return render(request, 'personal/signupd.html')

def login(request):
	return render(request, 'personal/login.html')
