#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse
from historicos.models import Usuario, Historico
from django.template import RequestContext, loader

# Create your views here.


def f2 (request):
    return HttpResponse('Funcao 2.')

def show_users(request):
    usuarios = Usuario.objects.all().order_by('nome_usuario')
    template = loader.get_template('show_users.html')
    context = RequestContext(request, {'usuarios': usuarios})
    return HttpResponse(template.render(context))


def show_histories(request, nome_usuario_proc):
    usuario_atual = Usuario.objects.get(nome_usuario=nome_usuario_proc)
    histories = Historico.objects.filter(usuario=usuario_atual)
    template = loader.get_template('show_histories.html')
    context = RequestContext(request, {'histories': histories, 'usuario': usuario_atual})
    return HttpResponse(template.render(context))


def show_histories_year(request, nome_usuario_proc, ano_proc):
    usuario_atual = Usuario.objects.get(nome_usuario=nome_usuario_proc)
    histories = Historico.objects.filter(usuario=usuario_atual, data__year=ano_proc)
    template = loader.get_template('show_history_year.html')
    context = RequestContext(request, {'histories': histories, 'usuario': usuario_atual, 'ano': ano_proc})
    return HttpResponse(template.render(context))
    

def show_histories_year_month(request, nome_usuario_proc, ano_proc, mes_proc):
    usuario_atual = Usuario.objects.get(nome_usuario=nome_usuario_proc)
    histories = Historico.objects.filter(usuario=usuario_atual, data__year=ano_proc, data__month=mes_proc)
    template = loader.get_template('show_history_year_month.html')
    context = RequestContext(request, {'histories': histories, 'usuario': usuario_atual, 'ano': ano_proc, 'mes': mes_proc})
    return HttpResponse(template.render(context))

def show_histories_year_month_day(request, nome_usuario_proc, ano_proc, mes_proc, dia_proc):
    usuario_atual = Usuario.objects.get(nome_usuario=nome_usuario_proc)
    histories = Historico.objects.filter(usuario=usuario_atual, data__year=ano_proc, data__month=mes_proc, data__day=dia_proc)
    template = loader.get_template('show_history_year_month_day.html')
    context = RequestContext(request, {'histories': histories, 'usuario': usuario_atual, 'ano': ano_proc, 'mes': mes_proc, 'dia': dia_proc})
    return HttpResponse(template.render(context))


def show_histories_all(request):
    histories = Historico.objects.all().order_by('-data')
    template = loader.get_template('show_histories_all.html')
    context = RequestContext(request, {'histories': histories})
    return HttpResponse(template.render(context))


def show_histories_year_all(request, ano_proc):
    histories = Historico.objects.filter(data__year=ano_proc).order_by('-data')
    template = loader.get_template('show_histories_year_all.html')
    context = RequestContext(request, {'histories': histories, 'ano': ano_proc})
    return HttpResponse(template.render(context))


def show_histories_year_month_all(request, ano_proc, mes_proc):
    histories = Historico.objects.filter(data__year=ano_proc, data__month=mes_proc).order_by('-data')
    template = loader.get_template('show_histories_year_month_all.html')
    context = RequestContext(request, {'histories': histories, 'ano': ano_proc, 'mes': mes_proc})
    return HttpResponse(template.render(context))


def show_histories_year_month_day_all(request, ano_proc, mes_proc, dia_proc):
    histories = Historico.objects.filter(data__year=ano_proc, data__month=mes_proc, data__day=dia_proc).order_by('-data')
    template = loader.get_template('show_histories_year_month_day_all.html')
    context = RequestContext(request, {'histories': histories, 'ano': ano_proc, 'mes': mes_proc, 'dia': dia_proc})
    return HttpResponse(template.render(context))
