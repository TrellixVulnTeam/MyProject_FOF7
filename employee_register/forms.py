from django.contrib import messages
from django import forms
from django.core.validators import RegexValidator
#from nocaptcha_recaptcha.fields import NoReCaptchaField

class RegisterForm(forms.Form):
	
	def __init__(self,*args,**kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['first_name'] = forms.CharField(max_length=120)
		self.fields['last_name'] = forms.CharField(max_length=120)
		self.fields['company'] = forms.CharField(max_length=120)
		self.fields['company_email'] = forms.EmailField()
		self.fields['alternate_email'] = forms.EmailField()
		self.fields['phone'] = forms.CharField(max_length=15, validators=[RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')])
		self.fields['password'] = forms.CharField(max_length=32, widget=forms.PasswordInput)
		self.fields['confirm_password'] = forms.CharField(max_length=32, widget=forms.PasswordInput)
	
	def clean(self):
		if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
				raise forms.ValidationError('Input passwords does not match')	
		return self.cleaned_data
	'''
	class Meta:
		model = Register
		widgets = {'password' : forms.PasswordInput,'confirm_password' : forms.PasswordInput}	
		fields = '__all__'
	'''
	#captcha = NoReCaptchaField(gtag_attrs={'data-theme':'dark'})