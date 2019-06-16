from django.forms import ModelForm, DateTimeField, HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from api.models import Patient, Case, PrescriptionTemplate


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    recent_coming = DateTimeField(label='最近来访', required=False, disabled=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.helper = FormHelper()
        # self.helper.form_method = 'post'
        #
        # instance = kwargs.get('instance')
        # if instance is not None:
        #     last_case_record = instance.case_set.last()
        #     if last_case_record is not None:
        #         datetime_string = last_case_record.pub_date
        #         self.fields['last_record_time'].initial = datetime_string


class PatientFormValid(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'sex', 'age', 'phone_number']


class CaseForm(ModelForm):

    class Meta:
        model = Case
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['patient'].widget = HiddenInput()
        self.fields['pub_date'].disabled = True

        # self.helper = FormHelper()

        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', '保存病历'))


class CaseFormValid(ModelForm):
    class Meta:
        model = Case
        fields = ['patient', 'symptom', 'template', 'prescription']


class PrescriptionTemplateForm(ModelForm):
    class Meta:
        model = PrescriptionTemplate
        fields = '__all__'


class PrescriptionTemplateFormValid(ModelForm):
    class Meta:
        model = PrescriptionTemplate
        fields = '__all__'

