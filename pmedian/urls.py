from django.conf.urls import url
from django.contrib import admin
from pmedian import views

urlpatterns = [
    url(r'p_median$', views.p_median),
    url(r'conftaskp$', views.conftaskpRender, name='conftaskp'),
    ]