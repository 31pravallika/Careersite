from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from jobsite.models import User
from .models import Jobpost
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from django.contrib.auth.views import LoginView

# class CandidateLoginView(LoginView):
#     template_name = 'Jlogin.html'  # Path to the candidate login template

# class EmployerLoginView(LoginView):
#     template_name = 'Elogin.html'   # Path to the employer login template

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Password=request.POST['Password']
        type=request.POST['type']
        b=['Employer','employer','EMPLOYER']
        c=['Jobseeker','jobseeker','JOBSEEKER']
        user=auth.authenticate(username=Username,password=Password,type=type)
        if user is not None:
            a=User.objects.get(username=Username)
            if a.type in b:
                auth.login(request,user)
                messages.info(request,'Successfully logged in')
                return redirect('/')
            elif a.type in c:
                auth.login(request,user)
                messages.info(request,'Successfully logged in')
                return redirect('/chome')
                
        else:
            messages.info(request,'invalid credentials')
            return redirect('Elogin')
        
    return render(request,'login.html')
# def Jlogin(request):
#     if request.method=='POST':
#         Username=request.POST['Username']
#         Password=request.POST['Password']
#         b=['Jobseeker','jobseeker','JOBSEEKER']
#         user=auth.authenticate(username=Username,password=Password)
#         if user is not None:
#             a=User.objects.get(username=Username)
#             if a.type in b:
#                 auth.login(request,user)
#                 messages.info(request,'Successfully logged in')
#                 return redirect('/chome')
#             else:
#                 messages.info(request,'invalid credentials')
#                 return redirect('Jlogin')
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('Jlogin')
        
#     return render(request,'Jlogin.html')

# register method

def register(request):
    if request.method=='POST':
        Username=request.POST['Username']
        email=request.POST['email']
        Password1=request.POST['Password1']
        Password2=request.POST['Password2']
        utype=request.POST['type']
        a=['Employer','Jobseeker','employer','jobseeker','EMPLOYER','JOBSEEKER']
        b=['Employer','employer','EMPLOYER']
        c=['Jobseeker','jobseeker','JOBSEEKER']
        if len(Username)<6:
            messages.info(request,'username must be atleat 6 characters')
            return redirect('register')
        if len(Password1)<8:
            messages.info(request,'password should be atleat 8 characters')
            return redirect('register')
        try:
            validate_email(email)
        except:
            messages.info(request,'enter valid email')
            return redirect('register')
        if utype in a:
            pass
        else:
            messages.info(request,'enter valid type')
            return redirect('register')
        if Password1==Password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username is already taken') 
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:   
                user=User.objects.create_user(username=Username,password=Password1,email=email,type=utype)
                user.save()
                messages.info(request,'user created')
            return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
       
    return render(request,'register.html')
def logout(request):
    b=['Employer','employer','EMPLOYER']
    c=['Jobseeker','jobseeker','JOBSEEKER']
    Username=request.user.username
    a=User.objects.get(username=Username)
    if a.type in b:
        auth.logout(request)
        return redirect('/')
    else:
        auth.logout(request)
        return redirect('/chome')
def hire(request):
    if request.method=='POST':
        title=request.POST['Title']
        company=request.POST['Company']
        location=request.POST['Location']
        salary=request.POST['Salary']
        siteurl=request.POST['link']
        description=request.POST['Description']
        uid=request.user.id
        userid=User.objects.get(id=uid)
        job=Jobpost.objects.create(title=title,company=company,Location=location,Salary=salary,link=siteurl,Description=description,uid=userid)
        job.save()
        return redirect('/')

    return render(request,'hire.html')
def chome(request):
    return render(request,'chome.html')
def jobs(request):
    jobs=Jobpost.objects.all

    return render(request,'jobs.html',{'jobs':jobs})