from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
from django.core.paginator import Paginator
import re
import json


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

    date_regex = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z')
    for key, value in request_data.items():
        if type(value) is str and date_regex.match(value):
            request_data[key] = parse_datetime(value)

    obj_id = request_data.get('id', None)
    if obj_id:
        obj = get_object_or_404(model, pk=obj_id)
        obj_form = form(request_data, instance=obj)
    else:
        obj_form = form(request_data)
    is_valid = obj_form.is_valid()
    result = {'success': is_valid}
    if is_valid:
        saved_obj = obj_form.save()
        result['data'] = obj_to_dict(saved_obj)
    else:
        result['errors'] = str(obj_form.errors)
        result['non_field_errors'] = str(obj_form.non_field_errors)
    return JsonResponse(result)


def obj_delete(request, model):
    if request.method != 'GET':
        return raise_405(request.method)

    obj_id = int(request.GET.get('id', 0))
    obj = get_object_or_404(model, pk=obj_id)
    result = {
        'data': obj_to_dict(obj),
        'success': True
    }
    obj.delete()
    return JsonResponse(result)


def raise_405(method):
    return JsonResponse({'err': f'Invalid method: {method}'}, status=405)
