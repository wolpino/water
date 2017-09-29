from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^add/$', views.addtrip, name="addtrip"),
    url(r'^trip/$', views.trip, name="add"),
    url(r'^destination/(?P<number>\d+)/$', views.trip_page, name="tripinfo"),
    url(r'^join/(?P<number>\d+)/$', views.join, name="join"),

]