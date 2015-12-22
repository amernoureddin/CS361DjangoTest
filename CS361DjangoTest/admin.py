from django.contrib import admin
from CS361DjangoTest.models import Publisher, Author, Book
from CS361DjangoTest.models import Course, Teacher, Student

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
