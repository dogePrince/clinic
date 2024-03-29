from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Patient(models.Model):
    name = models.CharField('姓名', max_length=20)

    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    SEX_CHOICES = (
        (FEMALE, '女'),
        (MALE, '男'),
        (OTHER, '其他'),
    )
    sex = models.CharField('性别', max_length=2, choices=SEX_CHOICES, default=FEMALE)
    age = models.IntegerField('年龄')
    phone_number = models.CharField('电话', max_length=20, blank=True, null=True)
    register_date = models.DateTimeField('注册日期', default=timezone.now, blank=True)

    def __str__(self):
        return self.name


class PrescriptionTemplate(models.Model):
    name = models.CharField('名称', max_length=20)

    def __str__(self):
        return self.name


class Case(models.Model):
    patient = models.ForeignKey(Patient, verbose_name='姓名', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('来访日期', default=timezone.now)
    symptom = models.TextField('症状', blank=True, null=True)
    template = models.ForeignKey(PrescriptionTemplate, verbose_name='方剂', on_delete=models.SET_NULL, blank=True, null=True)
    prescription = models.TextField('处方', blank=True, null=True)

    def __str__(self):
        return f'{self.patient.name}，{self.symptom}'
