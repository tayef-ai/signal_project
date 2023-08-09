from django.shortcuts import render
from .models import MyUser
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

def createuser(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            un = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            pw2 = fm.cleaned_data['confirm_password']
            if pw != pw2:
                messages.error(request, "Passwords Do Not Match")
                return HttpResponseRedirect('/')
            else:
                reg = MyUser(username=un, email=em, password=make_password(pw))
                reg.save()
                fm = UserForm()
    else:
        fm = UserForm()
    return render(request, 'signalapp/home.html', {'form':fm})
