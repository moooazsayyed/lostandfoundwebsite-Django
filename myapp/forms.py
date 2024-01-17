from django import forms
from .models import Listing

class UploadImg(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('title', 'image', 'description', 'categorie', 'state', 'email', 'phone_number')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'formbold-form-input'}),
            'image': forms.FileInput(attrs={'class': 'custum-file-upload'}),
            'image': forms.FileInput(attrs={'class': 'icon'}),
            'description': forms.Textarea(attrs={'class': 'formbold-form-input2'}),
            'categorie': forms.Select(attrs={'class': 'dropdown formbold-form-input'}),
            'state': forms.Select(attrs={'class': 'dropdown formbold-form-input'}),
            'email': forms.EmailInput(attrs={'class': 'formbold-form-input3'}),
            'phone_number': forms.TextInput(attrs={'class': 'formbold-form-input4'}),
        }