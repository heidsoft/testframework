# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
                        (r'^dashboard$','dashboard'),
                        (r'^hello$','hello'),
                        (r'^$', 'index'),
                        (r'^queryHost', 'queryHost'),
                        (r'^grid$', 'grid'),
                        (r'^forms$', 'forms'),
                        (r'^dev-guide/$', 'dev_guide'),
                        (r'^contactus/$', 'contactus'),
                        (r'^useradd', 'useradd'),
                        (r'^userlist', 'userlist'),
                        (r'^execute/task$', 'executeTask'),
                        (r'^execute/job$', 'executeJob'),
                        (r'^hosts$', 'getHosts'),
                        (r'^jobs', 'getJobs'),
)
