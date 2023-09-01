from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField


class Valueform(forms.Form):
    user = forms.CharField(max_length=100)
    last_name = forms.SlugField()
