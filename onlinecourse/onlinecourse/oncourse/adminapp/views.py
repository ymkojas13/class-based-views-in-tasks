from django.shortcuts import render, HttpResponseRedirect,redirect
from .forms import Signform
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

class sign_up(View):
    def post(self,request):
        fm = Signform(request.POST)
        if fm.is_valid():
            messages.success(request, 'you have signup successfully')
            fm.save()
        return render(request, 'signup.html', {'form': fm})

    def get(self, request):
        fm = Signform()
        return render(request, 'signup.html', {'form': fm})

class user_login(View):
    #if not request.user.is_authenticated:
    def post(self, request):
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/profile')
        #return render(request, 'login.html', {'form': fm})
    def get(self, request):
        fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})

    else:
        return HttpResponseRedirect('/login')

class user_logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')

