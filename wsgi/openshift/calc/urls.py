from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'calc.views.home', name='calc_home'),

    url(r'^get_data/','calc.views.couchdb_browser'),
    #Test CouchDB - pokazuje dane z CDB
    url(r'^couchdb_browser/','calc.views.couchdb_browser'),
    url(r"^check/(?P<job_id>[\w\-]+)/$", "calc.views.checkjob"),

)
