from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'chat.views.home', name='chat_home'),
    url(r'^data/', 'chat.views.data', name='data'),
    url(r'^add_task/', 'chat.tasks.init_work', name='add_task'),
    url(r'^task/','chat.views.task', name='task'),
    url(r'^delete_task/','chat.tasks.delete_job',name='delete_task'),
    
    url(r'^add_message', 'chat.views.add_message', name='add_message'),

    #Test CouchDB - pokazuje dane z CDB
    url(r'^couchdb_browser/','chat.views.couchdb_browser'),
    url(r'^get_message/','chat.tasks.get_message',)

)
