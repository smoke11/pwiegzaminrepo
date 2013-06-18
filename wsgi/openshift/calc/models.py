from django.core import serializers
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User

class Oblicz(models.Model):
    uuid=models.CharField(max_length=50)
    number1=models.FloatField()
    number2=models.FloatField()

    def json_decode(self, jsondata):
        self.uuid=jsondata['id']
        self.number1=jsondata['number1']
        self.number2=jsondata['number2']

    def json_encode(self):
        dict={}
        dict['id']=self.uuid
        dict['number1']=self.number1
        dict['number2']=self.number2
        return dict

    def __unicode__(self):
        return str(self.number1)+" "+str(self.number2)


class Wynik(models.Model):
    uuid=models.CharField(max_length=50)
    success=models.BooleanField()
    result=models.FloatField()

    def json_decode(self, jsondata):
        self.success=jsondata['success']
        self.result=jsondata['result']

    def json_encode(self):
        dict={}
        dict['success']=self.success
        dict['result']=self.result
        return dict

    def __unicode__(self):
        return str(self.success)+", wynik: "+str(self.result)