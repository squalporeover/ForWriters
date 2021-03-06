from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'age')#UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age') #UserChangeForm.Meta.fields


class CustomLoginForm(AuthenticationForm):
    #username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'kudfkj'})
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password.widget.attrs.update({ "class" : "form-control", 'id' : 'exampleInputEmail12'})
