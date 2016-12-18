from django.db import models

# Create your models here.


class Learn(models.Model):
    # db_index=True - создать индекс
    # unique=True - все строки уникальные
    # blank=True - разрешить пустое значение в поле (только для полей с данными, не для клбчей)
    # null=True - разрешить пустое значение во внешнем ключе (не в поле с данными)
    date_end = models.DateField(verbose_name='Дата окончания', auto_now=False, auto_now_add=False, db_index=True)
    site = models.CharField(verbose_name='Ссылка на сайт', max_length=128)
    name = models.TextField(verbose_name='Учреждение', max_length=1500)
    speciality = models.CharField(verbose_name='Специальность', max_length=128)

class Organization(models.Model):
    name = models.TextField(verbose_name='Организация', max_length=1500) # Место работы
    region = models.CharField(verbose_name='Регион', max_length=64) # Регион работы/фирмы
    site = models.CharField(verbose_name='Ссылка на сайт', max_length=128, blank=True) # Ссылка
    address = models.TextField(verbose_name='Адрес', max_length=1500, blank=True) # Адрес

class Work(models.Model):
    date_start = models.DateField(verbose_name='Дата начала работы', auto_now=False, auto_now_add=False, db_index=True)
    date_end = models.DateField(verbose_name='Дата окончания работы', auto_now=False, auto_now_add=False)
    organization = models.ForeignKey(Organization, verbose_name='Ссылка на организацию', on_delete=models.SET_NULL, null=True) # Связь многое-к-одному
    position = models.CharField(verbose_name='Должность', max_length=128) # Должность
    descr = models.TextField(verbose_name='Описание/Обязанности') # Описание
