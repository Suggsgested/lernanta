from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
  url(r'^(?P<status_id>\d+)/$', 'statuses.views.show',
      name='statuses_show'),
  url(r'^create/$', 'statuses.views.create',
      name='statuses_create'),
  url(r'^create/course/(?P<project_id>\d+)/$',
      'statuses.views.create_project_status',
      name='statuses_create_project'),
)
