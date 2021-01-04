from django.shortcuts import render
from .models import Newuser



# Create your views here.
def Indexpage(request):
    return render(request,'index.html')
    
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        
        age=request.POST.get['age']
        gender=request.POST.get['gender']
        password1=request.POST.get['password1']
        password2=request.POST.get['password2']
        if password1=password2:
            Newuser(username=username,email=email,password=password1,gender=gender,age=age).save()
            messages.success(request,'the New User'+request.POST['username']+"is save success")
    return render(request,'registration.html')
        
    
        
def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'],password=request.POST['password'])
            print("Username",Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username/password Invalid')
    return render(request,'login.html')
    
    
    
    