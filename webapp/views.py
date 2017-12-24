from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import signuppf, signupdf, loginf
from webapp.models import patient_info, doctor_info
from django.contrib.auth.models import User
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
			
			return HttpResponseRedirect('/login_view/')
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
			Chamber_address = request.POST.get('Chamber address','')
			Speciality = request.POST.get('Speciality','')
			Degree = request.POST.get('Degree','')
			user = User.objects.create_user(username=form.cleaned_data['username'],
				password=form.cleaned_data['password']) #createing user
			spd = doctor_info(name = name, username = username, password = password, Chamber_address = Chamber_address, Speciality = Speciality, Degree = Degree)
			spd.save() # save data into database
			
			return HttpResponseRedirect('/login_view/')
	else:
		form = signupdf()
	
	return render(request, 'personal/signupd.html', {'form': form})

def login_view(request):
	form = loginf()
	if form.is_valid():
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = User.authenticate(username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])

		return HttpResponseRedirect('/userhome/')

	return render(request, 'personal/login.html', {'form': form})

def userhome(request):
	#data = patient_info.objects.all()
	#data = doctor_info.objects.all()
	return render(request, 'personal/userhome.html')