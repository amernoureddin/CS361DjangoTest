# coding=utf-8
from django.template.loader import get_template, render_to_string
from django.http import Http404, HttpResponse
from django.template import Template, Context
import datetime
import re


def hello(request):
    return HttpResponse('Hello World')


def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It's {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>lt is %s</body></html>" % now
    return HttpResponse(html)
'''


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it’ll be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)


# Assignment 1 #


def word_count(request, offset):
    if offset == 'software':
        return word_count(request, offset='Software_Article_Wiki.html')
    elif offset == 'physics':
        return word_count(request, offset='Physics_Article_Wiki.html')
    count = {}
    line = render_to_string(template_name=offset)
    line = re.sub('[^\w,\d+]+', " ", line).lower()
    word = line.split()
    for w in word:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    t = get_template('Main_Assignment_#1.html')
    html = t.render(Context({'c': count.items(), 'article_name': offset}))
    return HttpResponse(html)
