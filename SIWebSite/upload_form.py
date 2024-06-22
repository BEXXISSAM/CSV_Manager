from django import forms


class UploadFileForm (forms.Form):
    upload = forms.FileField(required=True,max_length=100,widget=forms.FileInput(attrs={'class':'form-control form-control-lg','accept':'.csv'}))