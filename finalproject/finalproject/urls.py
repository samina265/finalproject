from django.contrib import admin
from django.urls import path,include
from app1 import views 

from imageapp.views import upload_image
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_or_signup, name='login_or_signup'),  # Handle both registration and login
    path('home/', views.home, name='home'),
    path('login_or_signup/', views.login_or_signup, name='login_or_signup'),
    path('upload/', upload_image, name='upload_image'),
    #path('password-reset/', include('django.contrib.auth.urls')),  # Include Django's built-in password reset URLs
]