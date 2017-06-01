from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<id>\d*)portfolio$', views.index, name="portfolio"),
]
