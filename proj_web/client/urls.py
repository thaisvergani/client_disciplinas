from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^course/$', views.course, name='course'),
    url(r'^course/(?P<id>\d+)/$', views.course, name='course'),
]
