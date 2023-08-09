from django import forms
from .models import MyUser

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100, widget=(forms.PasswordInput(attrs={
                'class': 'form-control',
        })
    ))
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        }

    
