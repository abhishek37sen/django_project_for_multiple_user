from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from machinetestapp.models import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect



def showregistration(request):
    return render(request,'registration.html')

def save_user(request):
    if request.method =="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        role = int(request.POST.get("role"))
        email = request.POST.get("email")
        country = request.POST.get("country")
        password = request.POST.get("psw")
        nationality = request.POST.get("nationality")
        mobilenumber = int(request.POST.get("mobile"))
        try:
            if role==1:
                user=CustomUser.objects.create_user(username=first_name+"_"+last_name,first_name=first_name,last_name=last_name,email=email,password=password,country=country,is_student=True,nationality=nationality,mobilenumber=mobilenumber)
            if role==2:
                user=CustomUser.objects.create_user(username=first_name+"_"+last_name,first_name=first_name,last_name=last_name,email=email,password=password,country=country,is_staff=True,nationality=nationality,mobilenumber=mobilenumber)
            if role==3:
                user=CustomUser.objects.create_user(username=first_name+"_"+last_name,first_name=first_name,last_name=last_name,email=email,password=password,country=country,is_admin=True,nationality=nationality,mobilenumber=mobilenumber)
            if role==4:
                user=CustomUser.objects.create_user(username=first_name+"_"+last_name,first_name=first_name,last_name=last_name,email=email,password=password,country=country,is_editor=True,nationality=nationality,mobilenumber=mobilenumber)
            user.save()
            messages.success(request,'Added Successfully')
            return render(request, 'login.html')
        except:
            messages.error(request, 'Failed to add user')
            return HttpResponse('User Not added')

    else:
        return HttpResponse("Method not Allowed")

def dologin(request):
    if request.method !="POST":
        return render(request,'login.html')
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user!=None:
            login(request,user)
            if user.is_admin:
                return redirect('adminpage')
                # return HttpResponse('admin_home')
            elif user.is_staff:
                return redirect('staff')
                # return HttpResponse('staff_home')
            elif user.is_student:
                return redirect('student')
                # return HttpResponse('student_home')
            elif user.is_editor:
                return redirect('editor')
                # return HttpResponse('student_home')
            else:
                return render(request,'login.html',{'error_message':"Invalid Login Details.."})
        else:
            return render(request, 'login.html', {"error_message": "Invalid Login Details.."})

def admin(request):
    user = request.user
    if user.is_authenticated and user.is_admin:
        return render(request,'admin.html')
    else:
        return render(request, 'login.html', {"error_message": "Admin Should be Login.."})


def student(request):
    user = request.user
    if user.is_authenticated and user.is_student:
        return render(request, 'student.html')
    else:
        return render(request, 'login.html', {"error_message": "Student Should be Login.."})



def staff(request):
    user = request.user
    if user.is_authenticated and user.is_staff:
        return render(request, 'staff.html')
    else:
        return render(request, 'login.html', {"error_message": "Staff Should be Login.."})

def editor(request):
    user = request.user
    msg = None
    if user.is_authenticated and user.is_editor:
        return render(request, 'editor.html')
    else:
        return render(request, 'login.html', {"error_message": "Editor Should be Login.."})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')