from django.shortcuts import redirect, render

from ..settings import WS
from ..forms.area import AreaForm
from ..client.area.rest import RestClient
from ..client.area.soap import SoapClient

if WS == 'SOAP':
    CLIENT = SoapClient

else:
    CLIENT = RestClient


def post_area(request):
    form = AreaForm(request.POST or None)
    client = CLIENT()

    if request.POST and form.is_valid():

        request_content = form.cleaned_data
        item_id = request.POST.get('item_id', None)

        if item_id:
            client.put(item_id, request_content)
        else:
            client.post(request_content)

    return redirect(get_all_areas)


def get_area(request, pk):
    client = CLIENT()
    data = client.get(pk)
    form = AreaForm(data)
    return render(request, 'area.html', {'form': form, 'item_id': pk, 'items': client.get()})


def delete_area(request, pk):
    client = CLIENT()
    data = client.get(pk)
    client.delete(data)
    return redirect(get_all_areas)


def get_all_areas(request):
    form = AreaForm(None)
    client = CLIENT()
    return render(request, 'area.html', {'form': form, 'items': client.get()})
