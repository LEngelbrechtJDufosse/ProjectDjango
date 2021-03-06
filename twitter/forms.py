from django import forms
from django.contrib.auth.models import User
from twitter.models import UserProfil, Tweet

class InscriptionForm (forms.ModelForm):
	password2 = forms.CharField(label = "Confirmation du mot de passe", max_length=100, widget=forms.PasswordInput)
        class Meta:
    		model = UserProfil
        	fields  = ['last_name','first_name','username', 'Avatar', 'email' , 'password', 'password2']
		widgets = {'password' : forms.PasswordInput()}

        def clean_password2(self):
		password1 = self.cleaned_data.get("password","")
		password2 = self.cleaned_data["password2"]
		if password1!=password2:
			raise forms.ValidationError("Les deux mots de passe sont differents")
		return password2

class LoginForm(forms.ModelForm):
	class Meta : 
		model = User
		fields = ['username', 'password']
		widgets = {'password' :  forms.PasswordInput(),}
	

class TweetForm (forms.ModelForm):
	class Meta:
   		model = Tweet
		fields = ['message']

class ModifForm (forms.ModelForm):
	class Meta : 
		model = UserProfil
		fields = ['last_name', 'first_name', 'username', 'Avatar', 'email']

class ModifPassword (forms.ModelForm):
	password2 = forms.CharField(label = "Confirmation du mot de passe", max_length=100)
	class Meta : 
		model = UserProfil
		fields = ['password', 'password2']
		widgets = {'password' : forms.PasswordInput(), 'password2' : forms.PasswordInput()}

	def clean_password2(self):
		password1 = self.cleaned_data.get("password","")
		password2 = self.cleaned_data["password2"]
		if password1!=password2:
			raise forms.ValidationError("Les deux mots de passe sont differents")
		return password2


