from django import forms
from login.models import Userinfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model =Userinfo
        fields = ('facebook_id','profile_picture')


