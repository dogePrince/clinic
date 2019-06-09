from django.contrib import admin
from .models import Patient, PrescriptionTemplate, Case


admin.site.register(Patient)
admin.site.register(PrescriptionTemplate)
admin.site.register(Case)
