from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1', 'password2']

        widgets={
            'username':forms.TextInput(attrs={'name':'form-control' , 'style':'display:block','placeholder':'Enter username'}),
            'first_name':forms.TextInput(attrs={'name':'form-control' , 'style':'display:block'}),
            'last_name':forms.TextInput(attrs={'name':'form-control' , 'style':'display:block'}),
            'email':forms.TextInput(attrs={'name':'form-control' , 'style':'display:block'}),
            'password1':forms.PasswordInput(attrs={'name':'form-control' , 'style':'display:block'}),
            'password2':forms.PasswordInput(attrs={'name':'form-control' , 'style':'display:block'}),
        }