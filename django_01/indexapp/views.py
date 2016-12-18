from django.shortcuts import render, render_to_response
from datetime import datetime, date
# Create your views here.

from .models import Work, Learn


def index(request):
    birth_date = date(1979, 8, 7)
    return render_to_response("index.html", {'birth_date': birth_date})


def learn(request):
    learn_places = Learn.objects.order_by('-date_end')
    return render_to_response("learn.html", {'learn_places': learn_places})


def org_card(request, num):
    work_places = Work.objects.values('date_start', 'date_end', 'position', 'descr', 'organization__name', 'organization__region', 'organization__site', 'organization__address').order_by('-date_start')
    return render_to_response("work.html", {'work_places': work_places})

def work(request):
    work_places = Work.objects.values('date_start', 'date_end', 'position', 'descr', 'organization__name', 'organization__region', 'organization__site', 'organization__address').order_by('-date_start')
    return render_to_response("work.html", {'work_places': work_places})
