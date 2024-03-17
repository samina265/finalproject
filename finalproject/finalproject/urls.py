from django.contrib import admin
from django.urls import path,include
from app1 import views 
from django.conf import settings
from django.conf.urls.static import static

from imageapp.views import upload_image
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_or_signup, name='login_or_signup'),
    path('home/', views.home, name='home'),
    path('login_or_signup/', views.login_or_signup, name='login_or_signup'),
    path('upload/', upload_image, name='upload_image'),
    path('main/', views.main, name='main'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)