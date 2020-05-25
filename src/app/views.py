from django.shortcuts import render
from django.core import serializers
import json
from datetime import datetime

from .models import Doctor
from .models import Patient
from .models import Test
from .models import TrackingChart


def index(request):
    return render(request, 'pages/index.html', {})

def personal(request):
    doctors_arr = Doctor.objects.all()
    doctors_json = serializers.serialize('json', doctors_arr)
    doctors_json = json.loads(doctors_json)
    for element in doctors_json:
        element['fields']['license_num'] = element['pk']
        fields = element['fields']
        element.clear()
        element.update(fields)
    #doctors_json = json.dumps(doctors_json)

    patients_arr = Patient.objects.all()
    patients_json = serializers.serialize('json', patients_arr)
    patients_json = json.loads(patients_json)
    for element in patients_json:
        element['fields']['primary_doctor'] = element['pk']
        fields = element['fields']
        element.clear()
        element.update(fields)
    #patients_json = json.dumps(patients_json)

def logic(request):
    doctors_arr = Doctor.objects.all()
    doctors_json = serializers.serialize('json', doctors_arr)
    doctors_json = json.loads(doctors_json)
    for element in doctors_json:
        element['fields']['license_num'] = element['pk']
        fields = element['fields']
        element.clear()
        element.update(fields)
    #doctors_json = json.dumps(doctors_json)

    patients_arr = Patient.objects.all()
    patients_json = serializers.serialize('json', patients_arr)
    patients_json = json.loads(patients_json)
    for element in patients_json:
        element['fields']['primary_doctor'] = element['pk']
        fields = element['fields']
        element.clear()
        element.update(fields)
    #patients_json = json.dumps(patients_json)

    tests_arr = Test.objects.all()
    tests_json = serializers.serialize('json', tests_arr)
    tests_json = json.loads(tests_json)
    for element in tests_json:
        element['fields']['code'] = element['pk']
        fields = element['fields']
        element.clear()
        element.update(fields)
    #tests_json = json.dumps(tests_json)

    # __lte = less then or equal
    tracking_arr = TrackingChart.objects.filter(due_date__lte=datetime.now())
    tracking_json = serializers.serialize('json', tracking_arr)
    tracking_json = json.loads(tracking_json)
    for element in tracking_json:
        fields = element['fields']
        element.clear()
        element.update(fields)

    all = {}
    all['doctors'] = doctors_json
    all['patients'] = patients_json
    all['tests'] = tests_json
    all['tracking'] = tracking_json
    all = json.dumps(all)

    context = {'doctors': doctors_arr,
               'patients': patients_arr,
               'tests': tests_arr,
               'tracking': tracking_arr,
               'all': all}

    return render(request, 'pages/logic.html', context)

def handler404(request, exception, template_name="pages/404.html"):
    #response = render_to_response(template_name)
    response = render(request, 'pages/404.html', {})
    response.status_code = 404
    return response

def handler400(request, exception, template_name="pages/400.html"):
    #response = render_to_response(template_name)
    response = render(request, 'pages/405.html', {})
    response.status_code = 400
    return response