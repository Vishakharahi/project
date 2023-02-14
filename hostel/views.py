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
phone=""
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
    global phone
    global em
    global fn
    global ln
    global sc
    global pwd
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
        
        if not HostelDetail.objects.filter(email=em):
             global otp1
             otp=random.randint(10000, 99999)
             otp1 = str(otp)
             print(otp1)

             if len(pwd) >= 8:
                if len(phone) == 10:
                            subject, from_email, to = 'Create Account', 'vishakharahi218@gmail.com',em
                            text_content = 'This is an important message.'
                            html_content = '<img src="https://www.web2sms.co.in/wp-content/uploads/2020/05/otpa.png" alt="img"> <br> Hi '+fn+' <br> Is Your One Time Password(OTP)<strong style="color:red;">'+otp1+ '</strong><br>Use For Create The Account Hostel'

                            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                            msg.attach_alternative(html_content, "text/html")
                            h=msg.send()
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
    print(phone)
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
             new.mobile=phone
             new.password=pwd            
             new.save()
             messages.success(request, 'Submited Successfully')
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
             request.session['lastname']=new[0].lastname
             request.session['email']=new[0].email
             messages.success(request, 'Login Successfully')
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
              firstname=request.POST.get('name')
              email=request.POST.get('email')
              message=request.POST.get('massage')
              new=Contactus()
              new.name=firstname
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


def Food_Menu(request):
    data=FoodMenu.objects.all().values()   
    print(data)
    cont={
        'item':data
    }
    return render(request,'FoodMenu.html',cont)
    

def profile(request):
            
    if request.method=='POST':
            updateid=request.session['id']
            image=request.FILES.get('image')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            studentcode=request.POST.get('studentcode')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            password=request.POST.get('password')
            member = HostelDetail.objects.get(id=updateid)
            member.firstname=firstname
            member.lastname=lastname
            member.image=image
            member.studentcode=studentcode
            member.email=email
            member.mobile=phone
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
         'phone':data[0].get('mobile'),
         'password':data[0].get('password')
         }
         return render(request,'profile.html',context)
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')   

# def department(request):
            
#     if request.method=='POST':
#             updateid=request.session['id']
#             Fullname=request.session['Fullname']
#             Field=request.POST.get('Field')
#             Semester=request.POST.get('Semester')
#             Timming=request.POST.get('Timming')
#             studentcode=request.POST.get('studentcode')
#             member = department.objects.get(id=updateid)
#             member.Fullname=Fullname
#             member.Field=Field
#             member.Semester=Semester
#             member.Timming=Timming
#             member.studentcode=studentcode
#             member.save()
            
#     id=request.session['id']   
#     if not id=="":
#          id=request.session['id']
#          data=department.objects.filter(id=id).values()
#          print(data[0].get('firstname'))
#          print(data[0].get('password'))
#          context = {
#          'Fullname':data[0].get('Fullname'),
#          'Field': data[0].get('Field'),
#          'Semester': data[0].get('Semester'),
#          'Timming':data[0].get('Timming'),
#          'studentcode':data[0].get('studentcode'),
#          }
#          return render(request,'department.html',context)
#     else:
#         messages.error(request,"Please Login or signups ")               
#         return redirect('/index')   



def department(request):
    if request.method =='POST':
              Fullname=request.POST.get('Fullname')
              Field=request.POST.get('Field')
              Semester=request.POST.get('Semester')
              studentcode=request.POST.get('studentcode')
              Timming=request.POST.get('Timming')
              new=studentdepartment()
              new. Fullname =Fullname
              new.Field=Field
              new.Semester=Semester
              new.studentcode=studentcode
              new.Timming=Timming
              new.save()
              messages.error(request,"Ok")
    return render(request,'department.html')



     
def fee_structure(request):
    
    Fees=Feestructure.objects.all().values()   
    print(Fees)
    cont={
        'items':Fees
    }
    return render(request,'fee_structure.html',cont)
        
def other_activity(request):
      if request.session['id']:
       return render(request,'other_activity.html')    
      else:
        messages.error(request,"Please Login or signups")         
        return redirect('/index')

def yoga(request):
      if request.session['id']:
       return render(request,'Yoga.html')    
      else:
        messages.error(request,"Please Login or signups")         
        return redirect('/index')

def picnic(request):
      if request.session['id']:
       return render(request,'Picnic.html')    
      else:
        messages.error(request,"Please Login or signups")         
        return redirect('/index')

def arts(request):
      if request.session['id']:
       return render(request,'Arts.html')    
      else:
        messages.error(request,"Please Login or signups")         
        return redirect('/index')
        
def games(request):
      if request.session['id']:
       return render(request,'Games.html')    
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
       return render(request,'Aboutus.html')    


def Feedback(request):
    if request.method =='POST':
              fn=request.POST.get('firstname')
              ln=request.POST.get('lastname')
              em=request.POST.get('email')
              country=request.POST.get('country')
              subject=request.POST.get('subject')
              new=feedback()
              new.firstname=fn
              new.ln=ln
              new.email=em
              new.country=country
              new.subject=subject
              new.save()
              messages.error(request,"Ok")
    return render(request,'Feedback.html')


def OURFOUNDERS(request):
    return render(request,'OURFOUNDERS.html')    
    
def OURAIM(request):
    return render(request,'OURAIM.html')    
     
def PRESIDENTSMESSAGE(request):
    return render(request,'PRESIDENTS MESSAGE.html')    
        
def GURUKULMANAGEMENTCOMMITTIEE(request):     
    return render(request,'GURUKULMANAGEMENTCOMMITTIEE.html')    
     
def COREVALUESOFGURUKUL(request):
    return render(request,'COREVALUESOFGURUKUL.html')    
        
def student_guidlines(request):
        if request.session['id']:
         return render(request,'student_guidlines.html')    
        else:
          messages.error(request,"Please Login or signups ")               
          return redirect('/index')
         

def hostel_booking(request):
    if request.session['id']:
        book=Booking.objects.all().values()   
        print(book)
        cont={
            'Booking':book
        }
        return render(request,'hostel_booking.html',cont)
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')   
    


def select_room(request):
    if request.method=="POST":
        id=request.POST.get('room')
        select=Selectroom()
        select.Roomno=id
        select.save()

    if request.session['id']: 
        data=Booking.objects.all().values()
        context={
            "item":data
        }
        return render(request,'select_room.html',context) 
    else:
        messages.error(request,"Please Login or signups ")               
        return redirect('/index')   
   

def bookingform(request):
    if request.method =='POST':
              Roomno=request.POST.get('Roomno')
              fullname=request.POST.get('Fullname')
              fathername=request.POST.get('Fathername')
              mothername=request.POST.get('Mothername')
              email=request.POST.get('Email')
              city=request.POST.get('City')
              fatheroccupation=request.POST.get('Fatheroccupation')
              fathernumber=request.POST.get('Fathernumber')
              studentnumber=request.POST.get('Studentnumber')
              new=Bookingform()
              new.Roomno=Roomno
              new.Fullname=fullname
              new.Fathername=fathername
              new.Mothername=mothername
              new.Email=email
              new.City=city
              new.Fatheroccupation=fatheroccupation
              new.Fathernumber=fathernumber
              new.Studentnumber=studentnumber
              new.save()
              messages.error(request,"Ok")
    data=Selectroom.objects.all().order_by('-id').values()
    print(data[0].get('Roomno'))
    context={
        'item':data[0].get('Roomno')
    }
    return render(request,'bookingform.html',context)

def footer(request):
    return render(request,'footer.html')


def logout(request):
    request.session['id']=""
    messages.success(request, 'Logout Successfully')
    return redirect('/index')











    



    