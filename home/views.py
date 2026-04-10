from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimonial, FAQ

def home(request):
    # Database se data fetch karna
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    
    context = {
        'testimonials': testimonials,
        'faqs': faqs,
        'app_name': 'Ai Recruiter'
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html', {'title': 'About Us'})

def pricing(request):
    return render(request, 'home/pricing.html', {'title': 'Pricing Plans'})

def contact(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Yahan message save karne ki logic add kar sakte hain
        
    return render(request, 'home/contact.html', {'title': 'Contact Us'})