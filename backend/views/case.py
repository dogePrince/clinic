from django.views.decorators.csrf import csrf_exempt
from backend.models import Case
from backend.forms import CaseForm
from . import utils


def case(request):
    if request.method != 'GET':
        return utils.raise_405(request.method)

    page_num = int(request.GET.get('page', 0))
    patient_id = int(request.GET.get('patient_id', 0))
    patient_field = utils.check_param_true(request.GET.get('patient_field'))

    extra_field = {}
    if patient_field:
        extra_field['patient'] = case_to_patient_dict

    if patient_id:
        case_list = Case.objects.all().filter(patient__id=patient_id).order_by('-pub_date')
    else:
        case_list = Case.objects.all().order_by('-pub_date')
    if page_num:
        return utils.list_to_page_json(case_list, page_num, **extra_field)
    return utils.list_to_json(case_list)


def by_id(request, case_id):
    if request.method != 'GET':
        return utils.raise_405(request.method)

    patient_field = utils.check_param_true(request.GET.get('patient_field'))

    extra_field = {}
    if patient_field:
        extra_field['patient'] = case_to_patient_dict
    return utils.obj_by_id(request, Case, case_id, **extra_field)


@csrf_exempt
def save(request):
    return utils.obj_save(request, Case, CaseForm)


def delete(request):
    return utils.obj_delete(request, Case)


def case_to_patient_dict(case_obj):
    return utils.obj_to_dict(case_obj.patient)


def case_to_template_dict(case_obj):
    if case_obj.template is None:
        return {}
    return utils.obj_to_dict(case_obj.template)
