from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addauthor$', views.addauthor, name="addauthor"),
    url(r'^addbook$', views.addbook, name="addbook"),
    #url(r'^portfolio$', views.portfolio, name="portfolio"),  
]
