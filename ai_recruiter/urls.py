from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home app (Main landing pages)
    path('', include('home.urls')),
    
    # Accounts app (Login/Register)
    path('auth/', include('accounts.urls')),
]