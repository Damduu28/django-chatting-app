from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Create Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": "Username"}),
            'email': forms.EmailInput(attrs={"placeholder": "Email"}),
        }

class ProfileUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar']
        
        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Full Name"}),
            'username': forms.TextInput(attrs={"placeholder": "Username"}),
            'email': forms.EmailInput(attrs={"placeholder": "Email"}),
        }