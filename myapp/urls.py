from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('cars', views.cars, name='cars'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')
]
