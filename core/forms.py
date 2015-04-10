from django import forms 

class URLInputForm(forms.Form):
	long_url = forms.URLField()