from django.forms import ModelForm
from api.models import Patient, Case, PrescriptionTemplate


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'sex', 'age', 'phone_number']


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['patient', 'symptom', 'template', 'dose_num', 'prescription']


class PrescriptionTemplateForm(ModelForm):
    class Meta:
        model = PrescriptionTemplate
        fields = '__all__'
