import os
import socket
from celery.result import AsyncResult
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
import requests
from chat.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from chat.couchdb_methods import *
from chat.tasks import send_message, register_to_couchdb
from settings import HOST_NAME

def home(request):
    return render(request,'chathome.html',)

def data(request):
    lines=Message.objects.all().order_by('-timestamp')
    return render(request,'data.html',{'lines':lines,})

def home_redirect(request):
    return redirect(reverse('chat_home'))

def task(request):
    if 'job' not in request.GET:
        return redirect(reverse('chat_home'))
    job_id = request.GET['job']
    job = AsyncResult(job_id)
    data = job.result or job.state
    return render(request, 'echo.html',{'what':json.dumps(data),'job':job_id,})


@login_required
def add_message(request):
    user=str(request.user.username)
    message=Message(uuid=uuid4(), user=user, message=request.POST['message'], timestamp=timezone.now())
    message.save()
    send_message.delay(message.json_encode())

    #requests.post("http://localhost:8000/get_message/",data=message.json_encode()) #lokalnie do siebie
    return redirect(('chat_home'))

#dla szybkiego sprawdzenia czy couchdb stoi i jak z danymi na ktorych operujemy.
#by sprawdzic main bazy danych, czyli same dokumenty, to trzeba zrobic iteracje po SERVER (bez arg)
def couchdb_browser(request):
    return render(request, 'couchdb_browser.html',{'docs': get_chatData(True), 'chat':True}) #jezeli przegladam sobie dokument chat to true

