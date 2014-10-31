from django.shortcuts import render
from django.http import HttpResponse
from coursera.models import Student


def students_view(request):
    html = ""
    for student in Student.objects.all():
        html += '<p>%i: %s</p>' % (student.id, student.name)
    return HttpResponse(html)