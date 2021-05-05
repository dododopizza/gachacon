from django.contrib.auth.models import User
from django import forms
from . import models
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-form-label'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('first_name', 'last_name', 'age', 'photo')
        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InfoEditForm(forms.ModelForm):
    class Meta:
        model = models.Info
        fields = ('info',)
        widgets = {
            'info': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RoleEditForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = ('role',)
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))