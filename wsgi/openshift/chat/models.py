from django.core import serializers
from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.contrib.auth.models import User

class Message(models.Model):
    uuid=models.CharField(max_length=50)
    user=models.CharField(max_length=20)
    message=models.CharField(max_length=200)
    timestamp=models.DateTimeField()
    
    def json_decode(self, jsondata):
        self.uuid=jsondata['id']
        self.message=jsondata['message']
        self.user=jsondata['user']
        self.timestamp=jsondata['timestamp']

    def json_encode(self):
        dict={}
        dict['id']=self.uuid
        dict['user']=self.user
        dict['message']=self.message
        dict['timestamp']=self.timestamp
        return dict

    def __unicode__(self):
        return self.user+"("+str(self.timestamp)+"): "+self.message
    
