from django.conf.urls.defaults import *

urlpatterns = patterns('project.views',
        (r'^list_for_class/(?P<class_id>\d+)/$', 'projects_for_class'),
        url(r'^create/$', 'create_project', name='create_project'),
)