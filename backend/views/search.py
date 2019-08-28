from django.db.models import Max
from django.http import JsonResponse
from django.db.models import Q
from django.utils.dateparse import parse_datetime
from backend.models import Patient, Case, PrescriptionTemplate
from . import utils, patient, case
import re


def search(request, search_type):
    whitespace_break = re.compile(r' +')
    query_string = request.GET.get('query').strip()
    if len(query_string) == 0:
        query_items = []
    else:
        query_items = whitespace_break.split(query_string)
    query_set = set(query_items)

    int_query = set()
    sex_query = set()
    char_query = set()
    sex_regex = re.compile(r'^[女男]$')
    int_regex = re.compile(r'^\d+$')
    for item in query_set:
        if sex_regex.match(item):
            sex_query.add(item)
        elif int_regex.match(item):
            int_query.add(item)
        else:
            char_query.add(item)

    earliest = request.GET.get('earliest')
    if earliest and len(earliest) > 0:
        earliest = parse_datetime(earliest)
    latest = request.GET.get('latest')
    if latest and len(latest) > 0:
        latest = parse_datetime(latest)
    time_range = {'earliest': earliest, 'latest': latest}

    query_sets = {
        'char': char_query,
        'int': int_query,
        'sex': sex_query
    }
    page = int(request.GET.get('page', 1))

    if search_type == 'patient':
        return search_patient(query_sets, page)
    elif search_type == 'case':
        return search_case(query_sets, page, time_range)
    elif search_type == 'template':
        print(233)
        return search_template(query_sets, page)
    return JsonResponse({'err': 'invalid search type'}, status=404)


def search_patient(query_sets, page):
    q = Q()
    q = q & get_query(['age', 'phone_number'], query_sets['int'])
    q = q & get_query(['name'], query_sets['char'])
    q = q & get_sex_query(query_sets['sex'])

    objs = Patient.objects.filter(q).annotate(last_case=Max('case__pub_date')).order_by('-last_case')
    extra_field = {'recent': patient.patient_recent_case_dict}

    return utils.list_to_page_json(objs, page, **extra_field)


def search_case(query_sets, page, time_range):
    q = Q()
    q = q & get_query(['patient__name', 'template__name', 'symptom', 'prescription'], query_sets['char'])
    q = q & get_query(['patient__name', 'template__name', 'symptom', 'prescription'], query_sets['sex'])
    q = q & get_query(['patient__name', 'template__name', 'symptom', 'dose_num', 'prescription'], query_sets['int'])

    range_kwargs = {}
    if time_range['earliest']:
        range_kwargs['pub_date__gte'] = time_range['earliest']
    if time_range['latest']:
        range_kwargs['pub_date__lte'] = time_range['latest']

    objs = Case.objects.filter(**range_kwargs).filter(q)

    extra_field = {'patient': case.case_to_patient_dict, 'template': case.case_to_template_dict}
    print(objs)
    return utils.list_to_page_json(objs, page, **extra_field)


def search_template(query_sets, page):
    q = Q()
    q = q & get_query(['name', 'prescription'], query_sets['int'])
    q = q & get_query(['name', 'prescription'], query_sets['char'])

    objs = PrescriptionTemplate.objects.filter(q)
    print(objs)
    return utils.list_to_page_json(objs, page)


def get_query(keys, query_set):
    q = Q()
    for query in query_set:
        sub_q = Q()
        for key in keys:
            sub_q = sub_q | Q(**{key + '__contains': query})
        q = q & sub_q
    return q


def get_sex_query(query_set):
    sexes = {'女': 'F', '男': 'M'}
    q = Q()
    for query in query_set:
        sub_q = Q()
        sub_q = sub_q | Q(**{'name__contains': query}) | Q(**{'sex__contains': sexes[query]})
        q = q & sub_q
    return q
