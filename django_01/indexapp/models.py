from django.db import models

# Create your models here.


class Learn(models.Model):
    date_end = models.DateField(verbose_name='Дата окончания', auto_now=False, auto_now_add=False, db_index=True)
    site = models.CharField(verbose_name='Ссылка на сайт', max_length=128)
    name = models.TextField(verbose_name='Учреждение', max_length=1500)
    speciality = models.CharField(verbose_name='Специальность', max_length=128)

class Work(models.Model):
    date_start = models.DateField(verbose_name='Дата начала работы', auto_now=False, auto_now_add=False, db_index=True)
    date_end = models.DateField(verbose_name='Дата окончания работы', auto_now=False, auto_now_add=False)
    site = models.CharField(verbose_name='Ссылка на сайт', max_length=128) # Ссылка
    name = models.TextField(verbose_name='Организация', max_length=1500) # Место работы
    region = models.CharField(verbose_name='Регион', max_length=64) # Регион работы/фирмы
    position = models.CharField(verbose_name='Должность', max_length=128) # Должность
    descr = models.TextField(verbose_name='Описание/Обязанности') # Описание
