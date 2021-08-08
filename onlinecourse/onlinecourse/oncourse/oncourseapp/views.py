from django.shortcuts import render,redirect
from .forms import onlineform
from .models import online
from django.contrib import messages
from django.views import View
from datetime import datetime, timedelta

class onlineco(View):
    def post(self,request):
        fm = onlineform(request.POST)
        if fm.is_valid():
            firstnm = fm.cleaned_data['Firstname']
            lastnm = fm.cleaned_data['Lastname']
            ema = fm.cleaned_data['Email']
            con = fm.cleaned_data['Contact']
            addr = fm.cleaned_data['Address']
            gen = fm.cleaned_data['Gender']
            pa = fm.cleaned_data['Password']
            conp = fm.cleaned_data['Confirm_password']
            soco = fm.cleaned_data['Software_courses']
            request.session['Firstname'] = firstnm
            request.session['Contact'] = con
            request.session['Address'] = addr
            onlinestore = online(Firstname=firstnm,Lastname=lastnm, Email=ema, Contact=con,Address=addr,Gender=gen,Password=pa,Confirm_password=conp,Software_courses=soco)
            onlinestore.save()
            messages.success(request, 'You have register successfully')
            det_view = online.objects.all()
            request.session['dicts'] = {'Firstname': firstnm, 'Contact': con}
            response = render(request, 'oncoursehtml.html', {'form': fm, 'details': det_view})
            response.set_cookie('Firstname', 'Murali krishna yadavalli', expires=datetime.utcnow() + timedelta(days=3))
            return response
    def get(self, request):
        fm = onlineform()
        data = online.objects.all()
        return render(request, 'oncoursehtml.html', {'form': fm, 'dataa': data})

class update_data(View):
    def post(self, request, id):
        pi=online.objects.get(pk=id)
        fm=onlineform(request.POST,instance=pi)
        if fm.is_valid():
            messages.success(request, 'You have update successfully')
            fm.save()
            return redirect('/oncourse')
    def get(self, request, id):
        pi=online.objects.get(pk=id)
        fm=onlineform(instance=pi)
        return render(request,'updateonline.html', {'form': fm})


class delete_data(View):
    def get(self, request, id):
        row = online.objects.get(pk=id)
        row.delete()
        return redirect('/oncourse')








