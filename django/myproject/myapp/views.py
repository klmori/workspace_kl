from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'welcome.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        print("Email:", email)
        print("Password:", password)
        return redirect('home')
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        print(request)
        return redirect('logout')
    return render(request, 'signup.html')

def home(request):
    return render(request, "home.html")

def verify(request):
    print(request)