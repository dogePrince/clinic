from django.urls import path

from . import views

app_name = 'cm'
urlpatterns = [
    # main page
    path('', views.index, name='index'),

    # for patient
    # path('patient', views.patient, name='patient'),
    path('patient/<int:patient_id>', views.patient_detail, name='patient_detail'),
    # path('patient/new', views.patient_new, name='patient_new'),

    # for case
    # path('case', views.case, name='case'),
    path('case/<int:case_id>', views.case_detail, name='case_detail'),
    # path('patient/<int:patient_id>/new_case', views.case_new, name='case_new'),

    # case queue
    # path('case_queue', views.case, name='case_queue'),

    # for test
    path('test', views.test, name='test'),
    path('test_vue', views.test_vue, name='test_vue'),
]
