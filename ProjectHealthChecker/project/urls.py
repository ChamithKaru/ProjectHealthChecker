__author__ = 'Thish'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<milestone_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^grid/$', views.grid, name='grid'),
    url(r'^imageTest/$', views.imageTest, name='imageTest'),
    url(r'^form/$', views.form, name='form'),
]
