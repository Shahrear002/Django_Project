from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import signuppf, signupdf, loginf
from webapp.models import patient_info, doctor_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
			user = User.objects.create_user(username=form.cleaned_data['username'],
				password=form.cleaned_data['password']) #creates user
			spo = patient_info(name = name, username = username, password = password, address = address, contactnumber = contactnumber)
			spo.save() # save data into database
			
			return HttpResponseRedirect('/login/')
	else:
		form = signuppf()
	
	return render(request, 'personal/signupp.html', {'form': form})

def signupd(request): # doctor's signup
	if request.method == 'POST':
		form = signupdf(request.POST)
		if form.is_valid(): 				#check validation
			name = request.POST.get('name','')
			username = request.POST.get('username','')
			password = request.POST.get('password','')
			Chamber_address = request.POST.get('Chamber_address','')
			Speciality = request.POST.get('Speciality','')
			Degree = request.POST.get('Degree','')
			user = User.objects.create_user(username=form.cleaned_data['username'],
				password=form.cleaned_data['password']) #createing user
			spd = doctor_info(name = name, username = username, password = password, Chamber_address = Chamber_address, Speciality = Speciality, Degree = Degree)
			spd.save() # save data into database
			
			return HttpResponseRedirect('/login/')
	else:
		form = signupdf()
	
	return render(request, 'personal/signupd.html', {'form': form})

def login_view(request):
	logout(request)
	form = loginf()
	username = password = ''
	if request.POST:
		#form.save()
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/userhome/')
		else:
			messages.error(request,"Invalid username or password, please try again.")
	else:
		form = loginf()

	return render(request, 'personal/login.html', {'form': form})

@login_required(login_url='/login/')
def userhome(request):
	data = doctor_info.objects.all()
	return render(request, 'personal/userhome.html', {'data': data})