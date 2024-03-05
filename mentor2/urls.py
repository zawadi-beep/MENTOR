
from django.contrib import admin
from django.urls import path
from mentor2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('index/', views.index,name='index')


]
