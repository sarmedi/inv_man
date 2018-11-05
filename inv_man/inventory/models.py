# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Inventory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Computer(models.Model):
    inventory=models.ForeignKey(Inventory, on_delete=models.CASCADE, default=None)
    manufacturer=models.CharField(max_length=20)
    serial_number=models.CharField(max_length=30)
    comments=models.CharField(max_length=500)
    def __str__(self):
        string1="This computer is made by "+self.manufacturer+",\nhas serial number: "+self.serial_number+",\nand is in Inventory: "+str(self.inventory)+"\nComments:\n"+self.comments
        return string1
