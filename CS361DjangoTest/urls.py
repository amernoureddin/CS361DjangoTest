"""CS361DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
# from django.conf.urls.defaults import *

from CS361DjangoTest.views import hello, current_datetime
from CS361DjangoTest.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^histogram/(?P<offset>\w+)/$', word_count),
    url(r'^histogram/software/$', word_count),
    url(r'^histogram/physics/$', word_count),
    url(r'^meta/$', display_meta),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
    url(r'^contact-form/$', contact_form),
    url(r'^contact/$', contact),
    url(r'^contactV2/$', contact_formsframework),
    url(r'^contact/thanks/$', hello),
    url(r'^addauthor/$', addauthor),
    url(r'^all-authors/$', all_authors),
    url(r'^addstudent/$', addstudent),
    url(r'^all-students/$', all_students),
    url(r'^addteacher/$', addteacher),
    url(r'^all-teachers/$', all_teachers),
    url(r'^addcourse/$', addcourse),
    url(r'^all-courses/$', all_courses),
    url(r'^enrollstudent/$', enrollstudent),
    url(r'^all-c-f-s/(?P<code>.+)/$', all_courses_for_student)

]
