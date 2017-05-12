from django.conf.urls import url
from django.contrib import admin
from general import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'signup$', views.signupRender, name='signup'),
    url(r'signin$', views.signin, name='signin'),
    url(r'logout$', views.logout),
    url(r'register$', views.register, name='register'),
    ]