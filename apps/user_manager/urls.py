from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.log_reg, name="entry"),    
    url(r'^main/$', views.log_reg, name="entry"),
    url(r'^login/$', views.login, name="log"),    
    url(r'^register/$', views.reg, name="reg"),        
    url(r'^(?P<number>\d+)/delete/$', views.delete, name="delete"),
    url(r'^logout/$', views.logout, name="peace"),
]