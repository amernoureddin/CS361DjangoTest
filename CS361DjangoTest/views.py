# coding=utf-8
from django.template.loader import get_template, render_to_string
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
import datetime
import re
from CS361DjangoTest.forms import *


def hello(request):
    print request.META
    if 'q' in request.GET:
        print request.GET['q']
    return HttpResponse('Hello World')


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % 'n'.join(html))


'''
def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It's {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''
'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>lt is %s</body></html>" % now
    return HttpResponse(html)
'''


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

'''
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>In %s hour(s), it’ll be %s.</body></html>' % (offset, dt)
    return HttpResponse(html)
'''


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', locals())


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


# End Assignment 1


# Forms #

def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_result.html', {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.' + '' + message)


def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})


def all_authors(request):
    return render_to_response('all_authors.html', {'author_list': Author.objects.all()})


def contact_form(request):
    return render_to_response('contact_form.html', RequestContext(request))


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            # send_mail(
            #      request.POST['subject'],
            #      request.POST['message'],
            #      request.POST['email'],
            #      ['ahmetbulut@gmail.com']
            # )
            return HttpResponseRedirect('/contact/thanks/', {}, RequestContext(request))
    return render_to_response('contact_form.html', {'errors': errors})


def contact_formsframework(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form2.html', {'form': form}, RequestContext(request))


def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            a = Author(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-authors/')
    else:
        form = AuthorForm()
    return render_to_response('addauthor.html', {'form': form}, RequestContext(request))

# End Forms #


# Assignment 3 #


def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = StudentForm()
    return render_to_response('addstudent.html', {'form': form}, RequestContext(request))


def all_students(request):
    return render_to_response('all_students.html', {'student_list': Student.objects.all()})


def addteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        office=form.cleaned_data["office"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = TeacherForm()
    return render_to_response('addteacher.html', {'form': form}, RequestContext(request))


def all_teachers(request):
    return render_to_response('all_teachers.html', {'teacher_list': Teacher.objects.all()})


def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Course(name=form.cleaned_data["name"],
                       code=form.cleaned_data["code"],
                       classroom=form.cleaned_data["classroom"],
                       times=form.cleaned_data["times"],
                       teacher=form.cleaned_data["teacher"]
                       # students=form.cleaned_data["students"]
                       )
            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = CourseForm()
    return render_to_response('addcourse.html', {'form': form}, RequestContext(request))


def all_courses(request):
    return render_to_response('all_courses.html', {'course_list': Course.objects.all()})


def enrollstudent(request):
    if request.method == 'POST':
        form = StudentToCourseForm(request.POST)
        if form.is_valid():

            a = form.cleaned_data["course"]
            b = Course.objects.get(code=a.code)
            b.students = form.cleaned_data["students"]

            return HttpResponseRedirect('/all-c-f-s/%s' % a.code)
    else:
        form = StudentToCourseForm()
    return render_to_response('enrollstudent.html', {'form': form}, RequestContext(request))


def all_courses_for_student(request, code):
    return render_to_response('all_courses_for_student.html', {'course': Course.objects.get(code=code)})


#################

# End Assignment 3 #
