from django.conf.urls import url

from .views import area, course, subject

urlpatterns = [
    url(r'^course/$', course.get_all_courses, name='course'),
    url(r'^course/post/$', course.post_course, name='post_course'),
    url(r'^course/get/(?P<pk>\d+)/', course.get_course, name='get_course'),
    url(r'^course/delete/(?P<pk>\d+)/', course.delete_course, name='delete_course'),

    url(r'^area/$', area.get_all_areas, name='area'),
    url(r'^area/post/$', area.post_area, name='post_area'),
    url(r'^area/get/(?P<pk>\d+)/', area.get_area, name='get_area'),
    url(r'^area/delete/(?P<pk>\d+)/', area.delete_area, name='delete_area'),

    url(r'^subject/$', subject.get_all_subjects, name='subject'),
    url(r'^subject/post/$', subject.post_subject, name='post_subject'),
    url(r'^subject/get/(?P<pk>\d+)/', subject.get_subject, name='get_subject'),
    url(r'^subject/delete/(?P<pk>\d+)/', subject.delete_subject, name='delete_subject'),
]
