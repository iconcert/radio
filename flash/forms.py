from django import forms
 
class Users(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    email = forms.EmailField()
    firstname = forms.CharField(label="Имя")
    lastname = forms.CharField(label="Фамилия", required=False)

class Autorization(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
