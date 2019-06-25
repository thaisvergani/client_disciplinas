from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^course/$', views.course, name='course'),
    url(r'^course/(?P<pk>\d+)/$', views.course, name='course'),
    url(r'^course/(?P<pk>\d+)/delete$', views.delete_course, name='delete_course'),
]
