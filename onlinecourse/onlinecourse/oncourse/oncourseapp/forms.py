from django import forms
from .models import online

class onlineform(forms.ModelForm):
    class Meta:
        model = online
        fields = '__all__'
        widgets={
            'Firstname':forms.TextInput(attrs={'class':'form-control'}),
            'Lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),
            'Confirm_password': forms.PasswordInput(render_value=True,attrs={'class': 'form-control'}),

        }