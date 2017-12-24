from django import forms

class signuppf(forms.Form):
	name = forms.CharField(required=True)
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	address = forms.CharField(required=True)
	contactnumber = forms.CharField(required=True)

	def clean(self):
		cleaned_data = super(signuppf, self).clean()
		name = cleaned_data.get('name')
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		address = cleaned_data.get('address')
		contactnumber = cleaned_data.get('contactnum')
		if not name and not username and not password and not address and not contactnumber:
			raise forms.ValidationError('You have to write something')
			
class signupdf(forms.Form):
	name = forms.CharField(required=True)
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)
	Chamber_address = forms.CharField(required=True)
	Speciality = forms.CharField(required=True)
	Degree = forms.CharField(required=True)

	def clean(self):
		cleaned_data = super(signupdf, self).clean()
		name = cleaned_data.get('name')
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		Chamber_address = cleaned_data.get('Chamber_address')
		Speciality = cleaned_data.get('Speciality')
		Degree = cleaned_data.get('Degree')
		if not name and not username and not password and not Chamber_address and not Speciality and not Degree:
			raise forms.ValidationError('You have to write something')
			
class loginf(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super(signupdf, self).clean()
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		if not username and not password:
			raise forms.ValidationError('You have to write something')