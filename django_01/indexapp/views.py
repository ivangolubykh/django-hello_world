from django.shortcuts import render, render_to_response
from datetime import datetime, date
from django.http import HttpResponse

from django.template import RequestContext
from django.template.context_processors import csrf
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
    if not request.session.get('work_count'):
        request.session['work_count'] = 'work_until_3'
    work_places = Work.objects.values('date_start', 'date_end', 'position', 'descr', 'organization', 'organization__name', 'organization__region', 'organization__address').order_by('-date_start')
    return render_to_response("work_ajax.html", RequestContext(request, {'work_places_first': work_places[:3], 'work_places_last': work_places[3:]}))


def work_ajax_change_view(request):
    if request.method == "POST":
        try:
            test_session_work_count = request.session.get('work_count')
            test_get_work_count = request.POST['work_count']
        except:
            test_session_work_count = 0
            test_get_work_count = 0

        if test_session_work_count and test_get_work_count == 'false':
            request.session['work_count'] = test_get_work_count
            return HttpResponse('', content_type='text/html')
        elif test_session_work_count and test_get_work_count == 'true':
            request.session['work_count'] = test_get_work_count
            work_places = Work.objects.values('date_start', 'date_end', 'position', 'descr', 'organization',
                                              'organization__name', 'organization__region',
                                              'organization__address').order_by('-date_start')[3:]
            return render_to_response("work_3_or_more.html", {'work_places': work_places})
        else:
            return HttpResponse('', content_type='text/html')
    else:
        return HttpResponse('', content_type='text/html')