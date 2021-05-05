from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileEditForm, LoginForm, InfoEditForm, RoleEditForm
from . import models
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = models.Profile.objects.create(user=new_user)
            info = models.Info.objects.create(user=new_user)
            role = models.Role.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def edit(request):
    if request.method == 'POST':
        role = models.Role.objects.get(user=request.user)
        info = models.Info.objects.get(user=request.user)
        info_form = InfoEditForm(instance=info , data=request.POST)
        role_form = RoleEditForm(instance=role , data=request.POST)
        profile = models.Profile.objects.get(user = request.user)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid() and role_form.is_valid() and info_form.is_valid():
            profile_form.save()
            role_form.save()
            info_form.save()
            return render(request, 'account/succesful.html')
        else:
            return render(request, 'account/error.html')
    else:
        role_form = RoleEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        info_form = InfoEditForm(instance=request.user)
        return render(request,
                      'account/edit.html',
                      {'profile_form': profile_form,
                      'role_form': role_form,
                      'info_form': info_form,
                      })
def profile(request):
    User = models.Profile.objects.get(user=request.user)

    role = models.Role.objects.get(user=request.user)
    info = models.Info.objects.get(user=request.user)
    return render(request, 'account/profile.html', {"profile": User,
    'role':role,
    'info':info,
    })