from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import signuppf
from webapp.models import signupp

def index(request):
	return render(request, 'personal/firstpage.html')

def signupp(request): # patient signup form view
	if request.method == 'POST':
		form = signuppf(request.POST)
		if form.is_valid():
			name = request.POST.get('name','')
			username = request.POST.get('username','')
			password = request.POST.get('password','')
			address = request.POST.get('address','')
			contactnumber = request.POST.get('contactnumber','')
			spo = signupp(name = name, username = username, password = password, address = address, contactnumber = contactnumber)
			spo.save() # save data into database
			

			return HttpResponseRedirect('personal/login.html')
	else:
		form = signuppf()
	
	return render(request, 'personal/signupp.html', {'form': form})

def signupd(request):
	return render(request, 'personal/signupd.html')

def login(request):
	return render(request, 'personal/login.html')
