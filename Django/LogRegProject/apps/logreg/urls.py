from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.log_register, name="register"),
    url(r'^login$', views.log_register, name="login"),
    url(r'^home$', views.home, name="home"),
    url(r'^logout$', views.logout, name="logout"),
]
