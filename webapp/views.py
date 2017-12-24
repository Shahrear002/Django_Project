from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import signuppf, signupdf, loginf
from webapp.models import patient_info, doctor_info

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
			spo = patient_info(name = name, username = username, password = password, address = address, contactnumber = contactnumber)
			spo.save() # save data into database
			
			return HttpResponseRedirect('personal/login.html')
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
			spd = doctor_info(name = name, username = username, password = password, Chamber_address = Chamber_address, Speciality = Speciality, Degree = Degree)
			spd.save() # save data into database
			
			return HttpResponseRedirect('personal/login.html')
	else:
		form = signupdf()
	
	return render(request, 'personal/signupd.html', {'form': form})

def login(request):
	if request.method == 'POST':
		form = loginf(request.POST)
		if form.is_valid():
			username = request.POST.get('username','')
			password = request.POST.get('password','')

			return HttpResponseRedirect('Thanks')
	else:
		form = loginf()

	return render(request, 'personal/login.html', {'form': form})
