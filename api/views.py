from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from api.models import Patient, Case, PrescriptionTemplate
from api.form import PatientForm, PatientFormValid
from django.core.paginator import Paginator
from django.db.models import Max
import datetime

date_time_format = "%Y-%m-%d %H:%M:%S"


def index(request):
    if request.method != 'GET':
        return raise_405(request.method)
    return HttpResponse("There will be API document in the future.")


def patient(request):
    if request.method != 'GET':
        return raise_405(request.method)

    page_num = int(request.GET.get('page', 1))
    patient_list = Patient.objects.annotate(last_case=Max('case__pub_date')).order_by('-last_case', '-register_date')

    paginator = Paginator(patient_list, 10)
    if page_num > paginator.num_pages:
        return raise_page_out_of_range(page_num, paginator.num_pages)
    page_obj = paginator.page(page_num)

    return JsonResponse(page_to_dict(page_obj))


def patient_by_id(request, patient_id):
    if request.method != 'GET':
        return raise_405(request.method)

    patient_obj = get_object_or_404(Patient, pk=patient_id)
    result = obj_to_dict(patient_obj)

    return JsonResponse(result)


def patient_save(request):
    if request.method != 'POST':
        return raise_405(request.method)

    print(request.POST)

    patient_id = request.POST.get('id', None)
    if patient_id:
        patient_obj = get_object_or_404(Patient, pk=patient_id)
        patient_form = PatientFormValid(request.POST, instance=patient_obj)
    else:
        patient_form = PatientFormValid(request.POST)
    is_valid = patient_form.is_valid()
    result = {'is_valid': is_valid}
    if is_valid:
        patient_form.save()

    return JsonResponse(result)


# utils methods
def to_json_value(value):
    if type(value) == datetime.datetime:
        return str(value)
    return value


def obj_to_dict(obj):
    result = dict()
    for field in obj._meta.fields:
        value = getattr(obj, field.name)
        value = to_json_value(value)
        result[field.name] = value

    if type(obj) == Patient:
        recent_case = obj.case_set.last()
        if recent_case is None:
            recent_coming = obj.register_date
        else:
            recent_coming = recent_case.pub_date
        result['recent_coming'] = to_json_value(recent_coming)
    return result


def page_to_dict(page_obj):
    result_list = list()
    for item in page_obj:
        result_list.append(obj_to_dict(item))

    result = {
        'list': result_list,
        'number': page_obj.number,
        'total': page_obj.paginator.num_pages
    }
    return result


def raise_405(method):
    return HttpResponse(f"Invalid method: {method}", status=405)


def raise_page_out_of_range(num, total):
    return HttpResponse(f'Page {num} out of range. (Total pages: {total})', status=404)
