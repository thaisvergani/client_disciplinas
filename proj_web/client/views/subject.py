from django.shortcuts import redirect, render

from ..settings import WS
from ..forms.subject import SubjectForm
from ..client.subject.rest import RestClient
from ..client.subject.soap import SoapClient
from ..client.area.rest import RestClient as AreaRestClient
from ..client.area.soap import SoapClient as AreaSoapClient
from ..client.courses.rest import RestClient  as CoursesRestClient
from ..client.courses.soap import SoapClient as CoursesSoapClient

if WS == 'SOAP':
    CLIENT = SoapClient
    AREAS_CLIENT = AreaSoapClient
    COURSES_CLIENT = CoursesSoapClient
else:
    CLIENT = RestClient
    AREAS_CLIENT = AreaRestClient
    COURSES_CLIENT = CoursesRestClient


def post_subject(request):
    # from IPython import embed; embed(),

    form = SubjectForm(data=request.POST or None,
                       courses=get_all_courses(),
                       areas=get_all_areas())
    client = CLIENT()

    if request.POST:
        if  form.is_valid():
            request_content = form.cleaned_data
            item_id = request.POST.get('item_id', None)
            request_content['curso'] = COURSES_CLIENT().get(request_content['curso'])
            request_content['area'] = AREAS_CLIENT().get(request_content['area'])
            if item_id:
                client.put(item_id, request_content)
            else:
                client.post(request_content)
        else:
            return render(request, 'subject.html', {'form': form,  'items': client.get()})

    return redirect(get_all_subjects)


def get_subject(request, pk):
    client = CLIENT()

    data = client.get(pk)
    data['curso'] = data['curso']['id']
    data['area'] = data['area']['id']
    form = SubjectForm(data=data,
                       courses=get_all_courses(),
                       areas=get_all_areas())
    return render(request, 'subject.html', {'form': form, 'item_id': pk, 'items': client.get()})


def delete_subject(request, pk):
    client = CLIENT()
    data = client.get(pk)
    client.delete(data)
    return redirect(get_all_subjects)


def get_all_subjects(request):
    form = SubjectForm(courses=get_all_courses(),
                       areas=get_all_areas())
    client = CLIENT()

    return render(request, 'subject.html', {'form': form, 'items': client.get()})


def get_all_courses():
    client = COURSES_CLIENT()
    items = client.get()

    return [(i.get('id'), i.get('nome')) for i in items]


def get_all_areas():
    client = AREAS_CLIENT()
    items = client.get()

    return [(i.get('id'), i.get('nome')) for i in items]
