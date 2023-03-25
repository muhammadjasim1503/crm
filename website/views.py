from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from .models import Record
from .forms import AddRecordForm

# Create your views here.

def home(request):
    records = Record.objects.all()
    # Check loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again!")
    return render(request,'home.html',{'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfuly!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Login
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registered successfuly!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})
    

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up records
        customer_record = Record.objects.get(id = pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "Authentication required!")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfuly!")
        return redirect('home')
    else:
        messages.success(request, "Authentication required!")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Added successfuly!')
                return redirect('home')

        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Authentication Required!")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id = pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Updated successfuly!')
                return redirect(f'/record/{pk}')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'Authentication required!')