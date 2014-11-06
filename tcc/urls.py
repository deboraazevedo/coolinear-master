# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tcc.views.home', name='home'),

    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^456/$', 'historicos.views.f2'),
    url(r'^$', 'historicos.views.show_histories_all', name='home'),
    url(r'^(?P<ano_proc>\d{4})/$', 'historicos.views.show_histories_year_all', name='user.history.year.all'),
    url(r'^(?P<ano_proc>\d{4})/(?P<mes_proc>\d{1,2})/$', 'historicos.views.show_histories_year_month_all', name='user.history.year.month.all'),
    url(r'^(?P<ano_proc>\d{4})/(?P<mes_proc>\d{1,2})/(?P<dia_proc>\d{1,2})/$', 'historicos.views.show_histories_year_month_day_all', name='user.history.year.month.day.all'),
    url(r'^usuarios/$', 'historicos.views.show_users', name="user.all"),
    url(r'^usuarios/(?P<nome_usuario_proc>\D{3,15})/$', 'historicos.views.show_histories', name="user.history"),
    url(r'^usuarios/(?P<nome_usuario_proc>\D{3,15})/(?P<ano_proc>\d{4})/$', 'historicos.views.show_histories_year', name='user.history.year'),
    url(r'^usuarios/(?P<nome_usuario_proc>\D{3,15})/(?P<ano_proc>\d{4})/(?P<mes_proc>\d{1,2})/$', 'historicos.views.show_histories_year_month', name='user.history.year.month'),
    url(r'^usuarios/(?P<nome_usuario_proc>\D{3,15})/(?P<ano_proc>\d{4})/(?P<mes_proc>\d{1,2})/(?P<dia_proc>\d{1,2})/$', 'historicos.views.show_histories_year_month_day', name='user.history.year.month.day'),


)


