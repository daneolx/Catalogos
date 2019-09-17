#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode, force_unicode
from django import forms

from django.db.models.signals import post_save
from django.dispatch import receiver

   
class segmento(models.Model):
    cod_segmento = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=500)

    def __unicode__(self):
        return str(self.pk)

class familia(models.Model):
	codseg = models.CharField(max_length=2)
	cod_familia = models.CharField(max_length=4)
	descripcion = models.CharField(max_length=500)

	def __unicode__(self):
		return str(self.pk)

class clase(models.Model):
	code = models.CharField(max_length=4)
	cod_clase = models.CharField(max_length=6)
	descripcion = models.CharField(max_length=500)
	def __unicode__(self):
		return str(self.pk)

class producto(models.Model):
	code = models.CharField(max_length=6)
	cod_producto = models.CharField(max_length=8)
	descripcion = models.CharField(max_length=500)
	def __unicode__(self):
		return str(self.pk)