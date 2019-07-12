from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from api.models import Patient, Case, PrescriptionTemplate
from api.form import PatientForm, CaseForm, PrescriptionTemplateForm
from django.core.paginator import Paginator
from django.db.models import Max
import datetime
import re


def index(request):
    if request.method != 'GET':
        return raise_405(request.method)
    return HttpResponse("There will be API document in the future.")


# patient
def patient(request):
    if request.method != 'GET':
        return raise_405(request.method)

    page_num = int(request.GET.get('page', 1))
    verbose = check_param_true(request.GET.get('verbose'))

    extra_field = {}
    if verbose:
        extra_field['recent'] = patient_recent_case_dict

    patient_list = Patient.objects.annotate(last_case=Max('case__pub_date')).order_by('-last_case', '-register_date')
    return list_to_page_json(patient_list, page_num, **extra_field)


def patient_by_id(request, patient_id):
    if request.method != 'GET':
        return raise_405(request.method)

    verbose = check_param_true(request.GET.get('verbose'))
    extra_field = {}
    if verbose:
        extra_field['recent'] = patient_recent_case_dict
    return obj_by_id(request, Patient, patient_id, **extra_field)


def patient_save(request):
    return obj_save(request, Patient, PatientForm)


# case
def case(request):
    if request.method != 'GET':
        return raise_405(request.method)

    page_num = int(request.GET.get('page', 1))
    verbose = check_param_true(request.GET.get('verbose'))

    extra_field = {}
    if verbose:
        extra_field['recent'] = case_to_patient_dict

    case_list = Case.objects.all().order_by('-pub_date')
    return list_to_page_json(case_list, page_num, **extra_field)


def case_by_id(request, case_id):
    if request.method != 'GET':
        return raise_405(request.method)

    verbose = check_param_true(request.GET.get('verbose'))

    extra_field = {}
    if verbose:
        extra_field['recent'] = case_to_patient_dict
    return obj_by_id(request, Case, case_id, **extra_field)


def case_save(request):
    return obj_save(request, Case, CaseForm)


# prescription template
def template(request):
    if request.method != 'GET':
        return raise_405(request.method)

    template_list = PrescriptionTemplate.objects.all().order_by('name')
    page_num = int(request.GET.get('page', 1))

    return list_to_page_json(template_list, page_num)


def template_by_id(request, template_id):
    return obj_by_id(request, PrescriptionTemplate, template_id)


def template_save(request):
    return obj_save(request, PrescriptionTemplate, PrescriptionTemplateForm)


# utils methods
def check_param_true(param):
    if type(param) is str:
        return re.match('true', param, re.I)
    return False


def to_json_value(value):
    if type(value) == datetime.datetime:
        return value.astimezone().strftime('%Y-%m-%d %H:%M:%S')
    if type(value) in (Patient, PrescriptionTemplate):
        return value.id
    return value


def obj_to_dict(obj, **kwargs):
    result = dict()
    for field in obj._meta.fields:
        value = getattr(obj, field.name)
        value = to_json_value(value)
        result[field.name] = value
    for key, fun in kwargs.items():
        result[key] = fun(obj)
    return result


def list_to_page_json(obj_list, page_num, per_page=10, **kwargs):
    paginator = Paginator(obj_list, per_page)
    if page_num > paginator.num_pages:
        page_num = paginator.num_pages
    page_obj = paginator.page(page_num)

    result_list = list()
    for item in page_obj:
        result_list.append(obj_to_dict(item, **kwargs))

    result = {
        'list': result_list,
        'per_page': per_page,
        'page_num': page_obj.number,
        'total_page': page_obj.paginator.num_pages
    }
    return JsonResponse(result)


def obj_by_id(request, model, obj_id, **kwargs):
    if request.method != 'GET':
        return raise_405(request.method)

    case_obj = get_object_or_404(model, pk=obj_id)
    result = obj_to_dict(case_obj, **kwargs)

    return JsonResponse(result)


def obj_save(request, model, form):
    if request.method != 'POST':
        return raise_405(request.method)

    obj_id = request.POST.get('id', None)
    if obj_id:
        obj = get_object_or_404(model, pk=obj_id)
        obj_form = form(request.POST, instance=obj)
    else:
        obj_form = form(request.POST)
    is_valid = obj_form.is_valid()
    result = {'success': is_valid}
    if is_valid:
        obj_form.save()
    return JsonResponse(result)


def patient_recent_case_dict(patient_obj):
    case_obj = patient_obj.case_set.last()
    return obj_to_dict(case_obj) if case_obj is not None else {}

def case_to_patient_dict(case_obj):
    return obj_to_dict (case_obj.patient)

def raise_405(method):
    return HttpResponse(f"Invalid method: {method}", status=405)


# def raise_page_out_of_range(num, total):
#     return HttpResponse(f'Page {num} out of range. (Total pages: {total})', status=404)
