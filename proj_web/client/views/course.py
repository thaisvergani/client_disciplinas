from django.shortcuts import redirect, render

from ..settings import WS
from ..forms.course import CourseForm
from ..client.courses.rest import RestClient
from ..client.courses.soap import SoapClient

if WS == 'SOAP':
    CLIENT = SoapClient

else:
    CLIENT = RestClient


def post_course(request):
    form = CourseForm(request.POST or None)
    client = CLIENT()

    if request.POST and form.is_valid():

        request_content = form.cleaned_data
        item_id = request.POST.get('item_id', None)

        if item_id:
            client.put(item_id, request_content)
        else:
            client.post(request_content)

    return redirect(get_all_courses)


def get_course(request, pk):
    client = CLIENT()
    data = client.get(pk)
    form = CourseForm(data)
    return render(request, 'course.html', {'form': form, 'item_id': pk, 'items': client.get()})


def delete_course(request, pk):
    client = CLIENT()
    data = client.get(pk)
    client.delete(data)
    return redirect(get_all_courses)


def get_all_courses(request):
    form = CourseForm(None)
    client = CLIENT()
    return render(request, 'course.html', {'form': form, 'items': client.get()})
