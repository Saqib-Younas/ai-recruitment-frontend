from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages

# Ye line lazmi hai taaki Django swapped model ko pehchaan sake
User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        # Data fetch karna
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        company_name = request.POST.get('company_name')
        company_size = request.POST.get('company_size')
        industry_type = request.POST.get('industry_type')
        location = request.POST.get('location')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Passwords match check
        if password != confirm_password:
            messages.error(request, "Passwords match nahi kar rahe!")
            return render(request, 'accounts/register.html')

        # Check if user exists by email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Ye email pehle se registered hai!")
            return render(request, 'accounts/register.html')

        # User create aur business data save karna
        try:
            # Custom model mein create_user call kar rahe hain
            user = User.objects.create_user(
                username=email, # Django username logic
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                position=position,
                company_name=company_name,
                company_size=company_size,
                industry_type=industry_type,
                location=location
            )
            user.save()
            
            # Registration ke baad login karwana
            login(request, user)
            messages.success(request, f"Welcome {first_name}! Account ban gaya hai.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Registration crash hui: {str(e)}")

    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username') 
        password = request.POST.get('password')
        # Django authenticate function standard 'username' parameter leta hai
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, "Ghalat Email ya Password!")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')