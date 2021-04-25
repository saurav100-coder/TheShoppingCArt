from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('careers', views.careers, name='careers'),
    path('register', views.get_customer, name='get_customer'),
    path('error', views.page_not_found, name='error'),
    path('test', views.test_page, name='test'),
 ]
