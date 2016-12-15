#!/usr/bin/env python3

from django.core.management.base import BaseCommand, CommandError
from indexapp.models import Work, Learn
import random


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
            amount = int(options['arg_command_line'][0])


            print(self.gen_string(amount))
