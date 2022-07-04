from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from backend.models import Patient
from backend.forms import PatientForm
from . import utils


def patient(request):
    if request.method != 'GET':
        return utils.raise_405(request.method)

    page_num = int(request.GET.get('page', 0))
    tiny_field = utils.check_param_true(request.GET.get('tiny_field'))
    recent_field = utils.check_param_true(request.GET.get('recent_field'))

    extra_field = {}
    if recent_field:
        extra_field['recent'] = patient_recent_case_dict

    patient_list = Patient.objects.annotate(last_case=Max('case__pub_date')).order_by('-last_case', '-register_date')
    if page_num:
        return utils.list_to_page_json(patient_list, page_num, **extra_field)
    if tiny_field:
        return utils.list_to_json(patient_list, ['id', 'name'])
    return utils.list_to_json(patient_list, **extra_field)


def by_id(request, patient_id):
    if request.method != 'GET':
        return utils.raise_405(request.method)

    recent_field = utils.check_param_true(request.GET.get('recent_field'))
    extra_field = {}
    if recent_field:
        extra_field['recent'] = patient_recent_case_dict
    return utils.obj_by_id(request, Patient, patient_id, **extra_field)


@csrf_exempt
def save(request):
    return utils.obj_save(request, Patient, PatientForm)


def delete(request):
    return utils.obj_delete(request, Patient)


def patient_recent_case_dict(patient_obj):
    case_obj = patient_obj.case_set.order_by('-pub_date').first()
    return utils.obj_to_dict(case_obj) if case_obj is not None else {}
