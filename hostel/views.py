from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .models import Contactus
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail,EmailMultiAlternatives
import random

fn=""
ln=""
sc=""
em=""
pwd=""
Field=""
Semester=""
Timming=""
otp1=""



#hostel index function
def index(request):    
    return render(request ,'index.html')
#hostel singup function
def signup(request):
    request.session['id']=""
    request.session['emailotp']=0
    if request.method == "POST":
        
        #imagename=image.name
        #ex=imagename.split('.')[1]
        #ex=ex.lower()
        #print(ex)
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        sc = request.POST['studentcode']
        em = request.POST['email']
        phone = request.POST['phone']
        pwd = request.POST['password']
        Field = request.POST['Field']
        Semester = request.POST['Semester']
        Timming = request.POST['Timming']
        if not HostelDetail.objects.filter(email=em):
             new=HostelDetail()
             new.firstname=fn
             new.lastname=ln
             new.studentcode=sc
             new.email=em
             new.password=pwd
             new.Field=Field
             new.Semester=Semester
             new.Timming=Timming
             new.save()
             global otp1
             otp=random.randint(10000, 99999)
             otp1 = str(otp)
             print(otp1)

             if len(pwd) >= 8:
                if len(phone) == 10:
                            subject, from_email, to = 'Create Account', 'tour.india1414@gmail.com',em
                            text_content = 'This is an important message.'
                            html_content = '<img src="https://cdn.pixabay.com/photo/2015/02/27/22/28/india-652857_960_720.png" alt="img"> <br> Hi '+fn+' <br> Is Your One Time Password(OTP)<strong style="color:red;">'+otp1+ '</strong><br>Use For Craete The Account India_Tour'

                            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                            msg.attach_alternative(html_content, "text/html")
                            h=msg.send()
                            print("tht")
                            if h:
                             return redirect('/otp')
                            else:
                                print("not work")
                            
                else:
                  messages.error(request, 'Mobile Number Should Only Contain 10 Number')

             else:
                messages.error(request, 'Password Must 8 Character Long !!!!')      
        else:
            messages.error(request, 'Email Is Already Exist')
                            
    return render(request,'registration.html')

def otp(request):
    #if not request.session[''] =="ghelo":
    print("hello")
    if request.method == "POST":
         rot=request.POST.get('enter')
         print(rot)
         rotp=str(rot)
         print(otp1)
         print(rotp)
         if rotp == otp1:
             new=HostelDetail()
             new.firstname=fn
             new.lastname=ln
             new.studentcode=sc
             new.email=em
             new.password=pwd
             new.Field=Field
             new.Semester=Semester
             new.Timming=Timming

             new.save()
             return redirect('/hostel_login')
         else:
             messages.error(request, 'Otp Are Incorrect')
       
    context={
            'email': em
            } 
    return render(request,'otp.html',context)
   # else:
    #        request.session['emailotp'] = 1
          #  return redirect('/index')
         #messages.error(request, 'Email Is Already Exist')                        
        



#hostel login fuction

def hostel_login(request):
    error =""
    if request.method == 'POST':
        print("hello")
        E = request.POST['email']
        P = request.POST['password']
        if HostelDetail.objects.filter(email=E):
           new=HostelDetail.objects.filter(email=E)
           print(new[0]) 
           pa=new[0].password
           if pa==P:
             request.session['id']=new[0].id
             request.session['name']=new[0].firstname
             request.session['email']=new[0].email
             return redirect('/hostel_home') 
           else:
             messages.error(request,"Enter Correct Password")
        
        else:
          messages.error(request,"User Does Not Exist")
                
    return render(request ,'hostel_login.html',locals())

#hostel home

def hostel_home(request):
    if request.session['id']:
       return render(request,'hostel_home.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')
    
def contact_us(request):
    if request.method =='POST':
              firstname=request.POST.get('firstname')
              email=request.POST.get('email')
              message=request.POST.get('massage')
              new=Contactus()
              new.firstname=firstname
              new.email=email
              new.message=message
              new.save()
              messages.error(request,"Ok")
    return render(request,'contact_us.html')





#hostel fuction

def hostel(request):
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        sc = request.POST['studentcode']
        em = request.POST['email']
        pwd = request.POST['password']
        if not HostelDetail.objects.filter(email=em):
             new=HostelDetail()
             new.firstname=fn
             new.lastname=ln
             new.studentcode=sc
             new.email=em
             new.password=pwd
             new.save()
             return redirect('/hostel_login') 
        else:
            messages.error(request, 'Email Is Already Exist')
                                
    return render(request,'hostel.html')


def info(request):
    if request.session['id']:
       return render(request,'info.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')

def images(request):
    if request.session['id']:
       return render(request,'images.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')


def Facilities(request):
    if request.session['id']:
       return render(request,'Facilities.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')


def FoodMenu(request):
    if request.session['id']:
       return render(request,'FoodMenu.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')


def profile(request):
            
    if request.method=='POST':
            updateid=request.session['id']
            image=request.FILES.get('image')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            studentcode=request.POST.get('studentcode')
            email=request.POST.get('email')
            password=request.POST.get('password')
            member = HostelDetail.objects.get(id=updateid)
            member.firstname=firstname
            member.lastname=lastname
            member.image=image
            member.studentcode=studentcode
            member.email=email
            member.password=password
            member.save()
            
    id=request.session['id']   
    if not id=="":
         id=request.session['id']
         data=HostelDetail.objects.filter(id=id).values()
         print(data[0].get('firstname'))
         print(data[0].get('password'))
         context = {
         
         'image': data[0].get('image'),
         'firstname': data[0].get('firstname'),
         'lastname':data[0].get('lastname'),
         'studentcode':data[0].get('studentcode'),
         'email':data[0].get('email'),
         'password':data[0].get('password')
         }
         return render(request,'profile.html',context)
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')   

def department(request):
            
    if request.method=='POST':
            updateid=request.session['id']
            Field=request.POST.get('Field')
            Semester=request.POST.get('Semester')
            Timming=request.POST.get('Timming')
            studentcode=request.POST.get('studentcode')
            member = HostelDetail.objects.get(id=updateid)
            member.Field=Field
            member.Semester=Semester
            member.Timming=Timming
            member.studentcode=studentcode
            member.save()
            
    id=request.session['id']   
    if not id=="":
         id=request.session['id']
         data=HostelDetail.objects.filter(id=id).values()
         print(data[0].get('firstname'))
         print(data[0].get('password'))
         context = {
         
         'Field': data[0].get('Field'),
         'Semester': data[0].get('Semester'),
         'Timming':data[0].get('Timming'),
         'studentcode':data[0].get('studentcode'),
         }
         return render(request,'department.html',context)
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')   
     

     
def fee_structure(request):
      if request.session['id']:
       return render(request,'fee_structure.html')    
      else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')
    
def other_activity(request):
      if request.session['id']:
       return render(request,'other_activity.html')    
      else:
        messages.error(request,"Please Login or signups")         
        return redirect('/index')
    
def change_password(request):
    if request.method=='POST':
            updateid=request.session['id']
            email=request.POST.get('email')
            password=request.POST.get('password')
            member = HostelDetail.objects.get(id=updateid)
            member.email=email
            member.password=password
            member.save()
            
    id=request.session['id']   
    if not id=="":
         id=request.session['id']
         data=HostelDetail.objects.filter(id=id).values()
         print(data[0].get('firstname'))
         print(data[0].get('password'))
         context = {
         'email':data[0].get('email'),
         'password':data[0].get('password')
         }
         return render(request,'change_password.html',context)
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index') 

def Aboutus(request):
    if request.session['id']:
       return render(request,'Aboutus.html')    
    else:
        messages.error(request,"Please Login or signups")         
        return redirect('/index')
    
def OURFOUNDERS(request):
    if request.session['id']:
        return render(request,'OURFOUNDERS.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')
    
def OURAIM(request):
     if request.session['id']:
        return render(request,'OURAIM.html')    
     else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')

def PRESIDENTSMESSAGE(request):
    if request.session['id']:
        return render(request,'PRESIDENTS MESSAGE.html')    
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')
    
def GURUKULMANAGEMENTCOMMITTIEE(request):
     if request.session['id']:
        return render(request,'GURUKULMANAGEMENTCOMMITTIEE.html')    
     else:
         messages.error(request,"Please Login or signups ")               
         return redirect('/index')

def COREVALUESOFGURUKUL(request):
        if request.session['id']:
         return render(request,'COREVALUESOFGURUKUL.html')    
        else:
          messages.error(request,"Please Login or signups ")               
          return redirect('/index')

def logout(request):
    request.session['id']=""
    return redirect('/index')











    



    