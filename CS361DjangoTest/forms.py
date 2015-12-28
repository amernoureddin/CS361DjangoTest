from django import forms
from models import *


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleanned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


class AuthorForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()


# Assignment 3 #


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()


class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    office = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()


class CourseForm(forms.Form):
    name = forms.CharField(max_length=100)
    code = forms.CharField(max_length=20)
    classroom = forms.CharField(max_length=100)
    times = forms.CharField(max_length=100)
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.all(), widget=forms.CheckboxSelectMultiple)


class CourseForm2(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class StudentForm2(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name


class StudentToCourseForm(forms.Form):
    students = StudentForm2(queryset=Student.objects.all())
    course = CourseForm2(queryset=Course.objects.all())

# class EnrollStudentsToCoursesForm(forms.Form):
#     students = forms.ModelMultipleChoiceField()
#     courses = forms.ModelMultipleChoiceField(queryset=)

# End Assignment 3 #
