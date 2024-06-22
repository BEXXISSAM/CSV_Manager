from django import forms
from .models import ImportFileModel

class ImportFileForm(forms.ModelForm):
    objects = None

    class Meta:
        model = ImportFileModel
        fields = ['date', 'file','activated']
