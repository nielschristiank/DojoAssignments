from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^result/$', views.result),
    url(r'^landscape/(?P<num>\d+)$', views.landscape)
]
