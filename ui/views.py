from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from api.form import PatientForm, CaseForm, PrescriptionTemplateForm
from api.models import Patient, Case, PrescriptionTemplate


def home(request):
    return render(request, 'ui/home.html')


def search(request):
    return render(request, 'ui/search.html')

def patient_detail(request, patient_id):
    return render(request, 'ui/patient.html')


def case_detail(request, case_id):
    case_form = CaseForm()
    patient_form = PatientForm
    content = {'case_form': case_form, 'patient_form': patient_form}

    return render(request, 'ui/common/case_form.html', content)


def test(request):
    # template_form = PrescriptionTemplateForm()
    # content = {'template_form': template_form}
    content = {}

    # return render(request, 'ui/patient/patient_new.html', content)
    # return render(request, 'ui/common/patient_form.html', content)
    return render(request, 'ui/components/patient_list.html', content)


def test_vue(request):
    return render(request, 'ui/test_vue.html')
