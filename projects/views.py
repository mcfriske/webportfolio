# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from webportfolio.quickstart import get_service

import datetime;
import re;

def index(request):
    return render(request, 'projects/index.html', {'title': 'Portfolio'})

def grid(request):
    return render(request, 'projects/grid.html', {'title': 'Grid Tiles', 'project': 'Grid Tiles'})

def blog(request):

    return render(request, "projects/blog.html", {'title': 'Blog', 'project': True})

def calendar(request):

    service = get_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=8, singleEvents=True,
        orderBy='startTime').execute()
    gcal = eventsResult.get('items', [])

    events = []
    time = False
    multiday = False

    for event in gcal:
        title = event.get('summary', 'Event')
        location = event.get('location', '')

        try:
            start = re.split('-[0-9]{2}:[0-9]{2}$', event['start']['dateTime'])[0]
            start = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
            end = re.split('-[0-9]{2}:[0-9]{2}$', event['end']['dateTime'])[0]
            end = datetime.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S')
            time = True
        except:
            start = event['start']['date']
            start = datetime.datetime.strptime(start, '%Y-%m-%d')
            end = event['end']['date']
            end = datetime.datetime.strptime(end, '%Y-%m-%d')
        description = event.get('description', '')

        if (start.strftime('%Y-%m-%d') != end.strftime('%Y-%m-%d')):
            multiday = True

        new_item = {'title': title,
                    'location': location,
                    'start': start,
                    'end': end,
                    'description': description,
                    'multiday': multiday,
                    'hasTime': time
                    }
        events.append(new_item)

    
    return render(request, "projects/calendar.html", {'title': 'Calendar', 
                                                      'project': True, 
                                                      'events': events})