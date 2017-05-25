from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^userpage$', views.userpage),
    url(r'^add_user/$', views.add_user)
]
