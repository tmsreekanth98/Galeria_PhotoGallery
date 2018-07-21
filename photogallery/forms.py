from django import forms
from .models import Photo

class ImportForm(forms.Form):
	title = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control import-form-title','placeholder':'Image Title'}))
	photo = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control import-form-title','placeholder':'Select Image'}))
	favorite = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-control'}))
	public = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class':'form-control','value':'Public'}))
