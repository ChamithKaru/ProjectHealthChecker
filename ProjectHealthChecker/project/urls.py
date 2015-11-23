__author__ = 'Thish'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<milestone_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^grid/$', views.grid, name='grid'),
]
