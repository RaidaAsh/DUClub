from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    url(r'^$', loungeHome),
    url(r'^search/$', search),
    url(r'^addLounge/$', addLounge),
    url(r'^loungeForm/$', addLng),
    url(r'^deleteLounge/$', deleteLounge),
    url(r'^deleteLng/$', deleteLng),
    url(r'^updateLounge/$', updateLounge),
    
    url(r'^add/$', addLoungePage),
    url(r'^delete/$', deleteLoungePage),
    url(r'^update/$', updateLoungePage),
]
