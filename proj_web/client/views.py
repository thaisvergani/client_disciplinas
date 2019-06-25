
from django.shortcuts import redirect, render

from .forms import CursoForm, AreaForm, DisciplinaForm, RestClient


def post_course(request):
    form = CursoForm(request.POST or None)
    client = RestClient()

    if request.POST and form.is_valid():

        request_content = form.cleaned_data
        item_id = request.POST.get('item_id', None)

        if item_id:
            client.put(item_id, request_content)
        else:
            client.post(request_content)

    return redirect(get_all_courses)


def get_course(request, pk):
    client = RestClient()
    data = client.get(pk)

    form = CursoForm(data)

    return render(request, 'base_form.html', {'form': form, 'item_id': pk, 'items': client.get()})


def delete_course(request, pk):
    client = RestClient()
    response = client.delete(pk)
    return redirect(get_all_courses)


def get_all_courses(request):
    form = CursoForm(None)
    client = RestClient()
    return render(request, 'base_form.html', {'form': form, 'items': client.get()})
