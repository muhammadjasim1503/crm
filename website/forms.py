from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label = '', max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = '', max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label = '', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email address'}))
    password1 = forms.CharField(label = '', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>')
    password2 = forms.CharField(label = '', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}), help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>')

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required = True, max_length=50, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name' }))
    last_name = forms.CharField(required = True, max_length=50, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name' }))
    email = forms.CharField(required = True, max_length=100, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email' }))
    phone = forms.CharField(required = True, max_length=15, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone' }))
    address = forms.CharField(required = True, max_length=100, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address' }))
    city = forms.CharField(required = True, max_length=50, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City' }))
    state = forms.CharField(required = True, max_length=50, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'State' }))
    zipcode = forms.CharField(required = True, max_length=20, label = '', widget= forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code' }))

    class Meta:
        model = Record
        exclude = ("user", "")