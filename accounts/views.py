from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Custom User model use karne ke liye
User = get_user_model()

def register_view(request):
    """
    Step 1: Basic Signup Logic
    Ismein Name, Email aur Password save hoga aur phir Company Info par redirect hoga.
    """
    if request.method == 'POST':
        # Data fetch karna
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Context taaki error par fields empty na hon
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        # 1. Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match! Please try again.")
            return render(request, 'accounts/signup.html', context)

        # 2. Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.warning(request, "This email is already registered. Please login or use another email.")
            # Yahan hum login par bhej rahe hain kyunki account pehle se hai
            return redirect('login')

        try:
            # 3. Create User
            user = User.objects.create_user(
                username=email, 
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            
            # 4. Automatically Log in the user
            login(request, user)
            
            # 5. Success Message & Redirect to Step 2 (Company Info)
            messages.success(request, f"Account created successfully! Now tell us about your company.")
            return redirect('company_info')
            
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'accounts/signup.html', context)

    return render(request, 'accounts/signup.html')

@login_required
def company_info_view(request):
    """
    Step 2: Company Details Logic
    User signup ke baad yahan aayega.
    """
    if request.method == 'POST':
        user = request.user
        user.position = request.POST.get('position')
        user.company_name = request.POST.get('company_name')
        user.company_size = request.POST.get('company_size')
        user.industry_type = request.POST.get('industry_type')
        user.location = request.POST.get('location')
        
        try:
            user.save()
            messages.success(request, "Profile completed! Welcome to your dashboard.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Error saving details: {str(e)}")

    return render(request, 'accounts/company_info.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


@login_required
def dashboard_view(request):
    """User Dashboard View with fixed data for template"""
    # Template ke liye lists taiyar karna
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Candidates ka data list of dictionaries mein
    candidates = [
        {'name': 'Andro Saimon', 'id': '#EROY586', 'email': 'androsaimon@gmail.com', 'location': 'England'},
        {'name': 'Jordan Maical', 'id': '#FGHZ896', 'email': 'jordanmaical@gmail.com', 'location': 'New York'},
        {'name': 'Raily Anderson', 'id': '#POIK787', 'email': 'railyanderson@gmail.com', 'location': 'Australia'},
        {'name': 'David Cooper', 'id': '#ULP6787', 'email': 'davidcooper@gmail.com', 'location': 'United States'},
        {'name': 'Maycal Jordern', 'id': '#NIO6789', 'email': 'maycaljordern@gmail.com', 'location': 'Australia'},
    ]

    context = {
        'first_name': request.user.first_name or "User",
        'applicants': 140,
        'emails': 100,
        'job_offers': 20,
        'months': months,
        'candidates': candidates,
    }
    return render(request, 'accounts/dashboard.html', context)