from django.shortcuts import render
from .models import Testimonial, FAQ

def home(request):
    """Landing Page with Testimonials and FAQs"""
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    
    context = {
        'testimonials': testimonials,
        'faqs': faqs,
        'app_name': 'Ai Recruiter'
    }
    return render(request, 'home/index.html', context)

def about(request):
    """About Us Page"""
    return render(request, 'home/about.html', {'title': 'About Us'})

def pricing(request):
    """Pricing Plans Page"""
    return render(request, 'home/pricing.html', {'title': 'Pricing Plans'})

def contact(request):
    """Contact Page with Form Handling"""
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Yahan message save ya email send karne ki logic add ho sakti hai
        
    return render(request, 'home/contact.html', {'title': 'Contact Us'})