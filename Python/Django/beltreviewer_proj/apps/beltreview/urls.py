from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^books$', views.home, name="home"),
    url(r'^books/add$', views.show_add_book, name="show_add_book"),
    url(r'^books/add/submit$', views.add_book, name="add_book"),
    url(r'^books/(?P<id>\d+)$', views.show_book, name="show_book"),
    url(r'^books/(?P<id>\d+)/add_review$', views.add_review, name="add_review"),
    url(r'^books/(?P<id>\d+)/delete_review$', views.delete_review, name="delete_review"),
    url(r'^user/(?P<id>\d+)$', views.show_user, name="show_user"),
]
