from django import forms
from .models import Run
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = ('activity','name', 'date', 'distance', 'duration')
        widgets = {
                'date': DateInput()
            }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(forms.Form, forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def clean_password(self):
        cd = self.data
        print(cd)
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords don\'t match!')
        return cd['password2']
