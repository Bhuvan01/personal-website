from django.urls import path
from . import views


urlpatterns = [
    
]

urlpatterns = [
path('', views.home, name = 'home'),
path('contact/',views.contact, name ='contact'),
path('about/',views.about, name ='about'),
path('portfolio/',views.portfolio, name ='portfolio'),
path('blog/',views.blog, name ='blog'),
path('signup/',views.signup_user, name ='signup'),
path('login/',views.login_user, name ='login'),
path('logout/',views.logout_user, name ='logout'),


]