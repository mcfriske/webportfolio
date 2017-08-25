# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    return render(request, 'projects/index.html', {'title': 'Portfolio'})

def grid(request):
    return render(request, 'projects/grid.html', {'title': 'Grid Tiles', 'project': 'Grid Tiles'})

def blog(request):

    return render(request, "projects/blog.html", {'title': 'Blog', 'project': True})