from django.forms import ModelForm
from backend.models import Patient, Case, PrescriptionTemplate


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'


class PrescriptionTemplateForm(ModelForm):
    class Meta:
        model = PrescriptionTemplate
        fields = '__all__'
