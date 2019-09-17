# -*- coding: utf-8 -*-
from principal.models import segmento, familia, clase, producto
#from principal.forms import ProfileForm, LlamadaForm, EditarContrasenaForm, VolanteForm, GestorForm, CierreLlamadaForm, LlamadaLogForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
from django.views import generic
from django.views.generic import TemplateView
import os
from catalogo.settings import STATIC_URL, BASE_DIR, MEDIA_ROOT
from django.template.loader import render_to_string
import cStringIO as StringIO
import cgi
import mimetypes
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime, date, time, timedelta
import sys
from django.contrib.auth.hashers import make_password
#from .forms import (EditarContrasenaForm)
import djqscsv
from djqscsv import render_to_csv_response
from django.utils import timezone
from django.utils.timesince import timesince
import calendar



def inicio(request):
	sege = segmento.objects.all()
	return render(request, "index.html", {'time':datetime.now(),'sege':sege})

def segmentos(request , codigo):
	sege = segmento.objects.filter(cod_segmento=codigo)
	fam = familia.objects.filter(codseg=codigo)
	clas = clase.objects.all()
	prod = producto.objects.all()
	return render(request, "index2.html", {'time':datetime.now() ,'sege':sege ,'fam':fam,'clas':clas,'prod':prod})

def familias(request , codigo):
	code = codigo[0:2]
	code2 = codigo[0:4]
	sege = segmento.objects.filter(cod_segmento=code)
	fam = familia.objects.filter(cod_familia=code2)
	clas = clase.objects.filter(code=codigo)
	prod = producto.objects.all()
	return render(request, "index3.html", {'time':datetime.now() ,'sege':sege ,'fam':fam,'clas':clas,'prod':prod,'code':code,'code2':code2})

def clases(request , codigo):
	code = codigo[0:2]
	code2 = codigo[0:4]
	code3 = codigo[0:6]
	sege = segmento.objects.filter(cod_segmento=code)
	fam = familia.objects.filter(cod_familia=code2)
	clas = clase.objects.filter(cod_clase=code3)
	prod = producto.objects.filter(code=codigo)
	return render(request, "index4.html", {'time':datetime.now() ,'sege':sege ,'fam':fam,'clas':clas,'prod':prod})

def productos(request , codigo):
	sege = segmento.objects.filter(cod_segmento=codigo)
	fam = familia.objects.filter(codseg=codigo)
	clas = clase.objects.all()
	prod = producto.objects.all()
	return render(request, "index2.html", {'time':datetime.now() ,'sege':sege ,'fam':fam,'clas':clas,'prod':prod})


def buscar(request):
    info = producto.objects.count()
    query = request.GET.get('q', '')
    prod2 = request.GET.get('q')
    if query:
        prod = producto.objects.filter(Q(descripcion__icontains=query))
    else:
        prod = []

    code = prod2[0:2]
    code2 = prod2[0:4]
    code3 = prod2[0:6]
    sege = segmento.objects.filter(cod_segmento=code)
    fam = familia.objects.filter(cod_familia=code2)
    clas = clase.objects.filter(cod_clase=code3)

    return render_to_response("index5.html", {'time':datetime.now(),
        "prod": prod,
        "sege":sege,
        "fam":fam,
        "clas":clas,
        "query": query,
        'info':info
    }, context_instance=RequestContext(request))


import services
class BooksPage(generic.TemplateView):
    def get(self,request):
        books_list = services.get_books('20511044121')
        return render(request,'books.html',books_list)