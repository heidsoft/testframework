# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'home_application.event.views',
    url(r'^type/$', 'type'),
    url(r'^manage/$', 'manage'),
)