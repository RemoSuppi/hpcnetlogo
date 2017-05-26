""" Defined URLs """

from django.conf.urls import url

from .views import JobListView, upload_job_view, stop, JobDeleteView, run

urlpatterns = [
    url(r'^$', JobListView.as_view(), name='job-list'),
    url(r'^upload/$', upload_job_view, name='job-upload'),
    url(r'^job/(?P<pk>[0-9]+)/delete/$', JobDeleteView.as_view(), name='del-job'),
    url(r'^job/(?P<id>[0-9]+)/run/$', run, name='run-job'),
    url(r'^job/(?P<id>[0-9]+)/stop/$', stop, name='stop-job'),
]
