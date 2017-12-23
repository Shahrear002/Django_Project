from django import forms

class signuppf(forms.Form):
	name = forms.CharField(required=True)
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
	address = forms.CharField(required=True)
	contactnum = forms.CharField(required=True)

	def clean(self):
		cleaned_data = super(signuppf, self).clean()
		name = cleaned_data.get('name')
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')
		address = cleaned_data.get('address')
		contactnum = cleaned_data.get('contactnum')
		if not name and not username and not password and not address and not contactnum:
			raise forms.ValidationError('You have to write something')
			
