from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import CourseForm



def course(request, id=None):
    if id:
        article = get_courses(pk=id)

    form = CourseForm(request.POST or None, instance=article)

    # if this is a POST request we need to process the form data
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        redirect_url = reverse(article_save_success)
        return redirect(redirect_url)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseForm()

    return render(request, 'base_form.html', {'form': form})

def get_courses(pk=None):