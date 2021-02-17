from django import  forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext,gettext_lazy as _


class loginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofcus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    

