# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Inventory Index.")

def detail(request, inven_name):
    return HttpResponse("You're looking at the inventory %s", % inven_name)

def create_comp(request, inven_id, comp_name, serial_num, comments):
    inven=get_object_or_404(Inventory, pk=inven_id)
    Inventory.computer_set.create(comp_name, serial_num, comments)
    return HttpResponse("You're creating computer %s", % comp_name)
