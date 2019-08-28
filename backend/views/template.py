from django.views.decorators.csrf import csrf_exempt
from backend.models import PrescriptionTemplate
from backend.forms import PrescriptionTemplateForm
from . import utils


def template(request):
    if request.method != 'GET':
        return utils.raise_405(request.method)

    template_list = PrescriptionTemplate.objects.all().order_by('name')
    page_num = int(request.GET.get('page', 0))
    tiny_field = utils.check_param_true(request.GET.get('tiny_field'))

    if page_num:
        return utils.list_to_page_json(template_list, page_num)
    if tiny_field:
        return utils.list_to_json(template_list, ['id', 'name'])
    return utils.list_to_json(template_list)


def by_id(request, template_id):
    return utils.obj_by_id(request, PrescriptionTemplate, template_id)


@csrf_exempt
def save(request):
    return utils.obj_save(request, PrescriptionTemplate, PrescriptionTemplateForm)


def delete(request):
    return utils.obj_delete(request, PrescriptionTemplate)
