# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    telphone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    ext = models.CharField(max_length=30)