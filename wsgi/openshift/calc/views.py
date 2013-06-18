import os
import socket
from celery.result import AsyncResult
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from couchdb_methods import get_calcData
from tasks import init_work


def home(request):
    try:
        calc = request.POST["calculation"]
        id = init_work(calc) #odwolywanie sie do tasks.init_stringwork(text)
        return redirect('calc.views.checkjob', job_id=id)
        #return render_to_response("testy/checkjob.html", {"job_id": str(id)}) #bo mi redirect nie dziala, a jest juz po polnocy :/
    except (KeyError):
        # Redisplay the form.
        return render_to_response("calc.html", context_instance=RequestContext(request))

def home_redirect(request):
    return redirect(reverse('calc_home'))

def checkjob(request, job_id):
    job = AsyncResult(job_id)
    data = '<b>Nie ma jeszcze wynikow, strona powinna sie odswiezyc za 3 sek, jesli tak sie nie stalo, to kliknij <a href="">TU</a>.</b>'
    if isinstance(job.result, dict):
        data = "Wynik:"+ str(job.result['value'])

    return render_to_response("checkjob.html", {"job": data, "job_id":job_id})



#dla szybkiego sprawdzenia czy couchdb stoi i jak z danymi na ktorych operujemy.
#by sprawdzic main bazy danych, czyli same dokumenty, to trzeba zrobic iteracje po SERVER (bez arg)
def couchdb_browser(request):
    return render(request, 'couchdb_browser.html',{'docs': get_calcData(True), 'calc':True}) #jezeli przegladam sobie dokument chat to true

