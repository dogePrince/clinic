from django.urls import path
from backend.views import search, patient, case, template

app_name = 'backend'
urlpatterns = [
    # for patient
    path('patient', patient.patient, name='patient'),
    path('patient/<int:patient_id>', patient.by_id, name='patient_by_id'),
    path('patient/save', patient.save, name='patient_save'),
    path('patient/delete', patient.delete, name='patient_delete'),

    # for case
    path('case', case.case, name='case'),
    path('case/<int:case_id>', case.by_id, name='case_by_id'),
    path('case/save', case.save, name='case_save'),
    path('case/delete', case.delete, name='case_delete'),

    # for case
    path('template', template.template, name='template'),
    path('template/<int:template_id>', template.by_id, name='template_by_id'),
    path('template/save', template.save, name='template_save'),
    path('template/delete', template.delete, name='template_delete'),

    # search
    path('search/<str:search_type>', search.search, name='search'),
]
