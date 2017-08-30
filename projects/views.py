# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from webportfolio.settings import BASE_DIR

import datetime;
import json;
import os;

def index(request):
    return render(request, 'projects/index.html', {'title': 'Portfolio'})

def grid(request):
    return render(request, 'projects/grid.html', {'title': 'Grid Tiles', 'project': 'Grid Tiles'})

def blog(request):

    return render(request, "projects/blog.html", {'title': 'Blog', 'project': True})

def calendar(request):
    path = os.path.join(BASE_DIR,'events.json')
    eventsResult = [];
    print(path)
    with open(path) as data_file:
        eventsResult = json.load(data_file)

    events = []
    time = None
    multiday = None

    for event in eventsResult:
        title = event.get('title', 'Event')
        location = event.get('location', '')

        start = event['start']
        end = event['end']

        try:
            start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
            end = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S')
            time = True
        except:
            start = datetime.datetime.strptime(start, '%Y-%m-%d')
            end = datetime.datetime.strptime(end, '%Y-%m-%d')
            time = False
        

        if (start.strftime('%Y-%m-%d') != end.strftime('%Y-%m-%d')):
            multiday = True
        else:
            multiday = False

        new_item = {'title': title,
                    'location': location,
                    'start': start,
                    'end': end,
                    'multiday': multiday,
                    'hasTime': time
                    }
        events.append(new_item)

    
    return render(request, "projects/calendar.html", {'title': 'Calendar', 
                                                      'project': True, 
                                                      'events': events})