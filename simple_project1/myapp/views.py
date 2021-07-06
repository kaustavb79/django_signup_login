from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

#login view
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Login Successfull!!!")
            return redirect('/profile/')
        else:
            messages.error(request, "Invalid username or password!!!!")
            return redirect('/login/')
    else:
        return render(request,'login.html')

#register user
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        #checking if username and password are correct
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!!!')
            return redirect('/register/')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!!!')
            return redirect('/register/')
        else:
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request,"user created successfully!!!")
            return redirect('/login/')    #redirecting to login/home page
    else:
        return render(request, 'register.html')

#profile view
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user.first_name})

#logout view
def user_logout(request):
    logout(request)
    messages.success(request," Logged Out Successfully!!!")
    return redirect('/login/')

