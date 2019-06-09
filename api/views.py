from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from api.models import Patient, Case, PrescriptionTemplate


def index(request):
    return HttpResponse("Root path of api for clinic.")


def obj_to_dict(obj):
    result = dict()
    for field in obj._meta.fields:
        value = getattr(obj, field.name)
        if type(value) not in (str, int):
            value = str(value)
        result[field.name] = value
    return result


def patient_detail(request, patient_id):
    if request.method not in ('POST', 'GET'):
        return HttpResponse(f"Invalid method: {request.method}", status=404)

    patient_obj = get_object_or_404(Patient, pk=patient_id)
    return JsonResponse(obj_to_dict(patient_obj))
