from django.shortcuts import render
from login import models
from login import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def index(request):
    data = {"title":"Home page"}
    if request.user.is_authenticated:
        current_user = request.user
        userID = current_user.id
        Userinfo = User.objects.get(pk=userID)
        userdetails = models.Userinfo.objects.get(user__pk=userID)
        data.update({"user":Userinfo,"userdetails":userdetails})
    return render(request,'login/index.html',context=data)
def loginpage(request):
    data = {"title":"Login page"}
    return render(request,'login/login.html',context=data)
def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("Worng data provides")
    else:
        return render(request,'login/login.html',context={"title":"Login page"})

@login_required
def UserLogout(request):
    logout(request)
    return redirect('/')

def registration(request):
    register = False
    if request.method == "POST":
        UserForm = forms.UserForm(data=request.POST)
        UserinfoForm = forms.UserInfoForm(data=request.POST)
        if UserForm.is_valid() and UserinfoForm.is_valid():
            user = UserForm.save()
            user.set_password(user.password)
            user.save()

            user_info = UserinfoForm.save(commit=False)
            user_info.user = user
            if 'profile_picture' in request.FILES:
                user_info.profile_picture = request.FILES['profile_picture']

            user_info.save()
            register = True
    else:
        UserForm = forms.UserForm()
        UserinfoForm = forms.UserInfoForm()

    data = {"title":"Registration page","LoginForm":UserForm,"UserForm":UserinfoForm,"register":register}
    return render(request,'login/registration.html',context=data)