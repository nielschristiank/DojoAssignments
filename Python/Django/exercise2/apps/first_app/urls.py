from django.conf.urls import url
from . import views

#Models -- Views -- TEMPLATES

urlpatterns = [
    url(r'^$', views.index)
]
