from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Max
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from api.models import Patient, Case, PrescriptionTemplate
from api.form import PatientForm, CaseForm, PrescriptionTemplateForm
import datetime
import re
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.method != 'GET':
        return raise_405(request.method)
    return HttpResponse("There will be API document in the future.")


# patient
def patient(request):
    if request.method != 'GET':
        return raise_405(request.method)

    page_num = int(request.GET.get('page', 0))
    tiny_field = check_param_true(request.GET.get('tiny_field'))
    recent_field = check_param_true(request.GET.get('recent_field'))

    extra_field = {}
    if recent_field:
        extra_field['recent'] = patient_recent_case_dict

    patient_list = Patient.objects.annotate(last_case=Max('case__pub_date')).order_by('-last_case', '-register_date')
    if page_num:
        return list_to_page_json(patient_list, page_num, **extra_field)
    if tiny_field:
        return list_to_json(patient_list, ['id', 'name'])
    return list_to_json(patient_list)


def patient_by_id(request, patient_id):
    if request.method != 'GET':
        return raise_405(request.method)

    recent_field = check_param_true(request.GET.get('recent_field'))
    extra_field = {}
    if recent_field:
        extra_field['recent'] = patient_recent_case_dict
    return obj_by_id(request, Patient, patient_id, **extra_field)


@csrf_exempt
def patient_save(request):
    return obj_save(request, Patient, PatientForm)


# case
def case(request):
    if request.method != 'GET':
        return raise_405(request.method)

    page_num = int(request.GET.get('page', 1))
    patient_id = int(request.GET.get('patient_id', 0))
    patient_field = check_param_true(request.GET.get('patient_field'))

    extra_field = {}
    if patient_field:
        extra_field['patient_field'] = case_to_patient_dict

    if patient_id:
        case_list = Case.objects.all().filter(patient__id=patient_id).order_by('-pub_date')
    else:
        case_list = Case.objects.all().order_by('-pub_date')
    return list_to_page_json(case_list, page_num, **extra_field)


def case_by_id(request, case_id):
    if request.method != 'GET':
        return raise_405(request.method)

    patient_field = check_param_true(request.GET.get('patient_field'))

    extra_field = {}
    if patient_field:
        extra_field['patient'] = case_to_patient_dict
    return obj_by_id(request, Case, case_id, **extra_field)


@csrf_exempt
def case_save(request):
    return obj_save(request, Case, CaseForm)


# prescription template
def template(request):
    if request.method != 'GET':
        return raise_405(request.method)

    template_list = PrescriptionTemplate.objects.all().order_by('name')
    page_num = int(request.GET.get('page', 0))
    tiny_field = check_param_true(request.GET.get('tiny_field'))

    if page_num:
        return list_to_page_json(template_list, page_num)
    if tiny_field:
        return list_to_json(template_list, ['id', 'name'])
    return list_to_json(template_list)


def template_by_id(request, template_id):
    return obj_by_id(request, PrescriptionTemplate, template_id)


@csrf_exempt
def template_save(request):
    return obj_save(request, PrescriptionTemplate, PrescriptionTemplateForm)


# utils methods
def check_param_true(param):
    if type(param) is str:
        return re.match('true', param, re.I)
    return False


def obj_to_dict(obj, fields=None, **kwargs):
    result = model_to_dict(obj)
    if fields is not None:
        result = {f: result[f] for f in fields}

    for key, fun in kwargs.items():
        result[key] = fun(obj)
    return result


def list_to_json(obj_list, fields=None, **kwargs):
    result_list = list()
    for item in obj_list:
        result_list.append(obj_to_dict(item, fields=fields, **kwargs))
    result = {
        'list': result_list,
        'count': len(obj_list)
    }
    return JsonResponse(result)


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

    obj = get_object_or_404(model, pk=obj_id)
    result = obj_to_dict(obj, **kwargs)
    return JsonResponse(result)


def obj_save(request, model, form):
    if request.method != 'POST':
        return raise_405(request.method)

    request_data = json.loads(request.body.decode())

    obj_id = request_data.get('id', None)
    if obj_id:
        obj = get_object_or_404(model, pk=obj_id)
        obj_form = form(request_data, instance=obj)
    else:
        obj_form = form(request_data)
    is_valid = obj_form.is_valid()
    result = {'success': is_valid}
    if is_valid:
        obj_form.save()
    else:
        result['errors'] = str(obj_form.errors)
        result['non_field_errors'] = str(obj_form.non_field_errors)
    return JsonResponse(result)


def patient_recent_case_dict(patient_obj):
    case_obj = patient_obj.case_set.last()
    return obj_to_dict(case_obj) if case_obj is not None else {}


def case_to_patient_dict(case_obj):
    return obj_to_dict(case_obj.patient)


def raise_405(method):
    return HttpResponse(f"Invalid method: {method}", status=405)


@csrf_exempt
def test(request):
    return
