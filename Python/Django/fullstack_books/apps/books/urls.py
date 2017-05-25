from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^book_data/$', views.submit_book)
]
