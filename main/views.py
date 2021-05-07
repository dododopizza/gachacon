from django.shortcuts import render, redirect
from account.models import Profile
from datetime import datetime

# Create your views here.

def index(request):
    form = Profile.objects.all()
    res = reversed(Profile.objects.filter(date_reg=int(datetime.today().strftime('%Y%m%d'))))
    try:
        id_user = request.user.id 
    except:
        id_user = False
    return render(request, "main/index.html", {
        'form' : form,
        'id':id_user,
        'res':res,
    })

def search(request):
    res = 0
    try:
        id_user = request.user.id 
    except:
        id_user = False
    form = Profile.objects.all()
    if request.method == "POST":
        res = Profile.objects.filter(role=request.POST['req'])
        return render(request, 'main/search.html',{
            'form': form,
            'res': res,
            'id':id_user,
        })
    return render(request, 'main/search.html', {
        'form': form,
        'res': res,
        'id':id_user,
    })
