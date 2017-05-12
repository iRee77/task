from django.conf.urls import url
from django.contrib import admin
from zmaps import views

urlpatterns = [
    url(r'index$', views.index),
    url(r'p_median$', views.p_median)
    ]