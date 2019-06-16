from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    # main page
    path('', views.index, name='index'),

    # for patient
    path('patient', views.patient, name='patient'),
    path('patient/<int:patient_id>', views.patient_by_id, name='patient_by_id'),
    path('patient/save', views.patient_save, name='patient_save'),

    # for case
    path('case', views.case, name='case'),
    path('case/<int:case_id>', views.case_by_id, name='case_by_id'),
    path('case/save', views.case_save, name='case_save'),

    # for case
    path('template', views.template, name='template'),
    path('template/<int:template_id>', views.template_by_id, name='template_by_id'),
    path('template/save', views.template_save, name='template_save'),

    # case queue
    # path('case_queue', views.case, name='case_queue'),

    # for test
    # path('test', views.test, name='test'),
]
