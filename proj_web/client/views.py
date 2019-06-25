import requests
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import CursoForm, AreaForm, DisciplinaForm


def course(request, pk=None):

    if pk:

        form = CursoForm()
        data = form.get(pk)
        form = CursoForm(data)

    else:
        form = CursoForm(request.POST or None)

        if request.POST and form.is_valid():

            request_content = form.cleaned_data
            form.post(request_content)

    return render(request, 'base_form.html', {'form': form, 'items': form.get()})


def get_course(request, pk):


    form = CursoForm()

    if request.POST and form.is_valid():
        request_content = form.cleaned_data
        form.post(request_content)

    return render(request, 'base_form.html', {'form': form, 'items': form.get()})


def delete_course(request, pk):
    form = CursoForm(None)
    response = form.delete(pk)
    return redirect(course)


def get_courses(pk=None):
    courses_base_url = "http://localhost:8080/universidade/rest/cursos"
    response = requests.get(courses_base_url, params={'id': pk})
    response = response.json()
    return response
