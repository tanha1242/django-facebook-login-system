from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  # <- Logout import

# Home Page
def homepage(request):
    return render(request, 'home.html')


# Signup Page
def signuppage(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        uname = (first_name + last_name).lower()
        email = request.POST.get('signupEmail')
        pass1 = request.POST.get('signupPassword')
        pass2 = request.POST.get('signupPassword2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'signup.html')

        my_user = User.objects.create_user(username=uname, email=email, password=pass1,
                                           first_name=first_name, last_name=last_name)
        my_user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'signup.html')


# Login Page
def loginpage(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('email')
        password = request.POST.get('password')

        user = None
        try:
            user_obj = User.objects.get(email=email_or_username)
            username = user_obj.username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = authenticate(request, username=email_or_username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Email/Username or Password is incorrect!")

    return render(request, 'login.html')


# Logout Page
def logoutpage(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
