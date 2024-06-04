# forms.py

from django import forms
from .models import Excel,Table1File

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Excel
        fields = ['file']

class UploadTable1FileForm(forms.ModelForm):
    class Meta:
        model = Excel
        fields = ['file']

class DownloadFileForm(forms.ModelForm):
    class Meta:
        model = Excel
        fields = ['file']


