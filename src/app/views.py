from django.shortcuts import render, redirect
from django.core import serializers
import json
from datetime import datetime

from .models import Doctor
from .models import Patient
from .models import Test
from .models import TrackingChart

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page 
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def model_serializer(model_arr, pk_id):
    """
    TBD.

    After applying this function 'json.dumps() function need to be applied.
    """
    json_string = serializers.serialize('json', model_arr)
    json_string = json.loads(json_string)
    i = 0
    for element in json_string:
        for field in element['fields']:
            # In case filed contain an object, serialize that object
            if (model_arr[i].__dict__.get(field) is None):
                # Get Object value by key in String type
                nested_obj = getattr(model_arr[i], field)
                nested_pk_id = nested_obj._meta.pk.name
                element['fields'][field] = model_serializer(
                    [nested_obj], nested_pk_id)[0]
        # When PK should go into the object
        if (pk_id):
            element['fields'][pk_id] = element['pk']
        # Final updates to clear not relevant parts of the given object
        fields = element['fields']
        element.clear()
        element.update(fields)
        i = i + 1
    return json_string

@cache_page(CACHE_TTL)
def index(request):
    """TBD."""
    return render(request, 'pages/index.html', {})


def personal(request):
    """TBD."""
    return redirect(recommendations)
    # doctors_arr = Doctor.objects.all()
    # patients_arr = Patient.objects.all()

@cache_page(CACHE_TTL)
def recommendations(request):
    """TBD."""
    # __lte = less then or equal
    recommendations_arr = TrackingChart.objects.filter(
        due_date__lte=datetime.now())
    recommendations_json = json.dumps(
        model_serializer(recommendations_arr, None))
    context = {'recommendations': recommendations_json}

    return render(request, 'pages/logic.html', context)


def handler404(request, exception, template_name="pages/404.html"):
    """TBD."""
    response = render(request, template_name, {})
    response.status_code = 404
    return response


def handler400(request, exception, template_name="pages/400.html"):
    """TBD."""
    response = render(request, template_name, {})
    response.status_code = 400
    return response
