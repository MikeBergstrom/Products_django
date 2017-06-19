# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=38)
    description = models.CharField(max_length=100)
    weight = models.CharField(max_length=38)
    price = models.CharField(max_length=38)
    cost = models.CharField(max_length=38)
    category = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
