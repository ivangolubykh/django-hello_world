#!/usr/bin/env python3
# Этот модуль можно вызвать командой "./manage.py gendatabd N" где N= от 1 до бесконечности
from django.core.management.base import BaseCommand, CommandError
from indexapp.models import Work, Learn
import random
from indexapp.models import Work, Learn, Organization
from datetime import date


class Command(BaseCommand):
    amount = 15; # кол-во добавляемых записей
    help = ('Модуль для заполнеия БД случаными данными в нужном количестве.\n'
            'Предусмотрен ровно один обязательный числовой параметр, отвечающий за кол-во генерируемых записей.\n'
            'Т.е. для генерации 15 записаей должно получиться так:\n'
            '"./manage.py gendatabd 15"')


    def gen_string(self, char_count):
        # В строку допустимых символов добавляю в среднем 1 пробел на 5 символов - это средняя длина слова
        symbol_string = ' абвгд еёжзи йклмн опрст уфхцч шщъыь эюя АБВГД ЕЁЖЗИ ЙКЛМН ОПРСТ УФХЦЧ ШЩЪЫЬ ЭЮЯ 01234 56789'
        rezault = ''
        for i in range(0, char_count):
            rezault += symbol_string[random.randint(0, (len(symbol_string) - 1))]
        return rezault

    def add_arguments(self, parser):
        parser.add_argument('arg_command_line', nargs='+', type=str)

    def handle(self, **options):
        if (not len(options['arg_command_line']) == 1) or (not options['arg_command_line'][0].isdigit()):
            print('ОШИБКА: должен быть ровно 1 числовой параметр, указывающий количество генерируемых записей. Например так:\n./manage.py gendatabd 15')
        else:
            amount = int(options['arg_command_line'][0]) + 1
            for i in range(1, amount ):
                data = Learn()
                data.date_end = date(random.randint(1980, 2016), random.randint(1, 12), random.randint(1, 28))
                data.site = 'http://' + str(i) + self.gen_string(random.randint(5, 128))
                data.name = str(i) + self.gen_string(random.randint(10, 1500))
                data.speciality = str(i) + self.gen_string(random.randint(0, 128))
                data.save()

                data = Organization()
                data.name = str(i) + self.gen_string(random.randint(10, 1500))
                data.region = str(i) + self.gen_string(random.randint(1, 64))
                data.site = 'http://' + str(i) + self.gen_string(random.randint(5, 128))
                data.address = str(i) + self.gen_string(random.randint(0, 1500))
                data.save()

                data = Work()
                data.date_start = date(random.randint(1980, 2016), random.randint(1, 12), random.randint(1, 28))
                # Не стал заморачиваться с тем, что дата увольнения может получиться раньше даты приёма на работу - для тестовых данных это не важно:
                data.date_end = date(random.randint(1980, 2016), random.randint(1, 12), random.randint(1, 28))
                data.position = str(i) + self.gen_string(random.randint(5, 64))
                data.descr = str(i) + self.gen_string(random.randint(5, 5007))
                data.organization = Organization.objects.get(id=(random.randint(1, i)))
#                data.organization = int(random.randint(1, i))
                data.save()

            print('Обработка завершена. В Work? d Organization и в Learn добавлено по ' + str(amount - 1) + ' новых записей')
