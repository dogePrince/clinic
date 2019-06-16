from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from api.models import Patient, Case, PrescriptionTemplate
from api.form import PatientFormValid, CaseFormValid, PrescriptionTemplateFormValid
from django.core.paginator import Paginator
from django.db.models import Max
import datetime


def index(request):
    if request.method != 'GET':
        return raise_405(request.method)
    return HttpResponse("There will be API document in the future.")


# patient
def patient(request):
    if request.method != 'GET':
        return raise_405(request.method)

    patient_list = Patient.objects.annotate(last_case=Max('case__pub_date')).order_by('-last_case', '-register_date')
    page_num = int(request.GET.get('page', 1))

    return list_to_page_json(patient_list, page_num)


def patient_by_id(request, patient_id):
    return obj_by_id(request, Patient, patient_id)


def patient_save(request):
    return obj_save(request, Patient, PatientFormValid)


# case
def case(request):
    if request.method != 'GET':
        return raise_405(request.method)

    case_list = Case.objects.all().order_by('-pub_date')
    page_num = int(request.GET.get('page', 1))

    return list_to_page_json(case_list, page_num)


def case_by_id(request, case_id):
    return obj_by_id(request, Case, case_id)


def case_save(request):
    return obj_save(request, Case, CaseFormValid)


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
    return obj_save(request, PrescriptionTemplate, PrescriptionTemplateFormValid)


# utils methods
def list_to_page_json(obj_list, page_num, num_per_page=10):
    paginator = Paginator(obj_list, num_per_page)
    if page_num > paginator.num_pages:
        return raise_page_out_of_range(page_num, paginator.num_pages)
    page_obj = paginator.page(page_num)

    return JsonResponse(page_to_dict(page_obj))


def obj_by_id(request, model, obj_id):
    if request.method != 'GET':
        return raise_405(request.method)

    case_obj = get_object_or_404(model, pk=obj_id)
    result = obj_to_dict(case_obj)

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
    result = {'is_valid': is_valid}
    if is_valid:
        obj_form.save()

    return JsonResponse(result)


def to_json_value(value):
    if type(value) == datetime.datetime:
        return str(value)
    if type(value) in (Patient, PrescriptionTemplate):
        return value.id
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
