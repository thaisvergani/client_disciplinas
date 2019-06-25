from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^course/$', views.get_all_courses, name='course'),
    url(r'^course/post/$', views.post_course, name='post_course'),
    url(r'^course/get/(?P<pk>\d+)/', views.get_course, name='get_course'),
    url(r'^course/delete/(?P<pk>\d+)/', views.delete_course, name='delete_course'),
]
