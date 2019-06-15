from django.forms import ModelForm, DateTimeField, HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from api.models import Patient, Case


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    last_record_time = DateTimeField(label='最近来访', required=False, disabled=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        instance = kwargs.get('instance')
        if instance is not None:
            last_case_record = instance.case_set.last()
            if last_case_record is not None:
                datetime_string = last_case_record.pub_date
                self.fields['last_record_time'].initial = datetime_string


class PatientFormValid(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'sex', 'age', 'phone_number']
