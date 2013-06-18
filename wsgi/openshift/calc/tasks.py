from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery import task, current_task
from celery.result import AsyncResult
from time import sleep
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf.urls import patterns, url
from django.shortcuts import render, get_object_or_404, redirect
jobs=[]


@task()
def compute(num1, num2, operator):
    current_task.update_state(state='PROGRESS', meta={'current': "working"})
    print 'computing: '+num1+operator+num2
    val=None
    num1=int(num1)
    num2=int(num2)
    if operator == '+':
        val=num1+num2
    elif operator == '-':
        val=num1-num2
    elif operator == '*':
        val=num1*num2
    elif operator == '/':
        val=num1/num2
    elif operator == '%':
        val=num1%num2
    print 'Value= '+str(val)
    return {'value':str(val)}

#def poll_state(request):
#    """ A view to report the progress to the user """
#    if 'job' in request.GET:
#        job_id = request.GET['job']
#    else:
#        return HttpResponse('No job id given.')
#
#    job = AsyncResult(job_id)
#    data = job.result or job.state
#    return HttpResponse(json.dumps(data), mimetype='application/json')

def init_work(value):
    calc = value
    job = compute.delay(calc[0],calc[2],calc[1])
    print 'append new job, id= '+job.id
    jobs.append(job.id)
    return job.id


def delete_job(request):
    if 'job' not in request.GET:
        return HttpResponse('No job id given.')
    job_id = request.GET['job']
    job=AsyncResult(job_id)
    jobs.remove(job)
    return redirect(reverse('home'))
        

#@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
#def clean_works():
#    for job in jobs:
#        if job.state=='SUCCESS':
#            jobs.remove(job)
