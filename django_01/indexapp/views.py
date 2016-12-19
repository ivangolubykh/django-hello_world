from django.shortcuts import render, render_to_response
from datetime import datetime, date
# Create your views here.

from .models import Learn, Organization, Work


def index(request):
    birth_date = date(1979, 8, 7)
    return render_to_response("index.html", {'birth_date': birth_date})


def learn(request):
    learn_places = Learn.objects.order_by('-date_end')
    return render_to_response("learn.html", {'learn_places': learn_places})


def org_card(request, num):
    org_places = Organization.objects.filter(id = num)
    return render_to_response("org_card.html", {'org_places': org_places})

def work(request):
    work_places = Work.objects.values('date_start', 'date_end', 'position', 'descr', 'organization', 'organization__name', 'organization__region', 'organization__address').order_by('-date_start')
    return render_to_response("work.html", {'work_places_first': work_places[:3], 'work_places_last': work_places[3:]})

def work_ajax(request):
    work_places = Work.objects.values('date_start', 'date_end', 'position', 'descr', 'organization', 'organization__name', 'organization__region', 'organization__address').order_by('-date_start')
    return render_to_response("work_ajax.html", {'work_places_first': work_places[:3], 'work_places_last': work_places[3:]})
