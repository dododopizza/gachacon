from django.contrib.auth.models import User
from django import forms
from . import models
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Повтори пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-form-label'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels ={
            'username': ('Имя пользователя'),
            'email': ('Email адрес')
        }
        help_texts = {
            'username': ('Обязательное поле. 16 символов и меньше. Буквы, цифры и @/./+/-/_ только.'),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class ProfileEditForm(forms.ModelForm):
    role = forms.ChoiceField(label='Роль:', widget=forms.Select(attrs={'class': 'form-control'}), choices=[
                ('Программист','Программист'),
                ('Дизайнер','Дизайнер')
            ])
    class Meta:
        model = models.Profile
        fields = ('age', 'photo','role','country','city','tools','interest','work_time', 'GMT','email')
        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'country':forms.TextInput(attrs={'class': 'form-control'}),
            'city':forms.TextInput(attrs={'class': 'form-control'}),
            'tools':forms.TextInput(attrs={'class': 'form-control'}),
            'interest':forms.TextInput(attrs={'class': 'form-control'}),
            'work_time':forms.TextInput(attrs={'class': 'form-control'}),
            'GMT':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'age': ('Возраст:'),
            'photo': ('Фото профиля:'),
            'role': ('Роль:'),
            'country': ('Страна:'),
            'city': ('Город:'),
            'tools': ('Инструменты:'),
            'interest': ('Интересы:'),
            'work_time': ('Рабочее время:'),
            'GMT': ('Часовой пояс по GMT:'),
            'email': ('Email:'),
        }




class ProjectsEditForm(forms.ModelForm):
    
    class Meta:
        model = models.Project
        fields = ('image','link','name_project', 'date')
        widgets = {
            "image" : forms.FileInput(attrs={'class': 'form-control'}),
            'link' : forms.TextInput(attrs={'class': 'form-control'}),
            'name_project': forms.TextInput(attrs={'class': 'form-control'}),
            'date' : forms.HiddenInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))