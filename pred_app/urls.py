from django.urls import path

from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
   ]
