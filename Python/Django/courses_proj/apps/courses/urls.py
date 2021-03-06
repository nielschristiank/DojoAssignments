from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course/$', views.add_course),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_course),
    url(r'^course/(?P<id>\d+)$', views.view_course, name = 'view_course'),
    url(r'^post_comment/(?P<id>\d+)$', views.post_comment)
]
