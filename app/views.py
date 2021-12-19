from django.http import request
from django.shortcuts import render
from .models import Registration
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def reg(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        hobbies=request.POST['hobbies']
        country=request.POST['country']
        address=request.POST['address']
        new_profile=Registration(username=username,email=email,password=password,confirm=confirm,fname=fname,
        lname=lname,gender=gender,hobbies=hobbies,country=country,address=address)
        new_profile.save()
        print(username)
        print(email)
        print(password)
        print(confirm)
        print(fname)
        print(lname)
        print(gender)
        print(hobbies)
        print(country)
        print(address)
        success = 'User '+ username + " created successsfully"
        return HttpResponse(success)
        