from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('home/', views.homepage, name='home'),
    path('signup/', views.signuppage, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),  # <- Logout URL
]
