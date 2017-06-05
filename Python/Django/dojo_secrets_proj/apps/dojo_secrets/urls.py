from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name = "login"),
    url(r'^logout$', views.logout, name = "logout"),
    url(r'^register$', views.register, name='register'),
    url(r'^secrets$', views.secrets, name='secrets'),
    url(r'^popular_secrets$', views.popular_secrets, name='popular_secrets'),
    url(r'^post_secret$', views.post_secret, name='post_secret'),
    url(r'^like/(?P<secret_id>\d+)$', views.like, name='like'),
    url(r'^delete_secret/(?P<id>\d+)$', views.delete_secret, name="delete_secret")
]
