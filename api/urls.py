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
    # path('case', views.case, name='case'),
    # path('case/<int:case_id>', views.case_detail, name='case_detail'),
    # path('patient/<int:patient_id>/new_case', views.case_new, name='case_new'),

    # case queue
    # path('case_queue', views.case, name='case_queue'),

    # for test
    # path('test', views.test, name='test'),
]
