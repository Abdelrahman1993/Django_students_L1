from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
import os

# Create your views here.
from django.http import HttpResponse
students = [
    {
        'id':1,
        'name': "abdo",
        'age': 25,
        'image': static('students/images/1.png')
    },
    {
        'id':2,
        'name': "ahmed",
        'age': 30,
        'image': static('students/images/2.jpeg')
    }
    ,
    {
        'id':3,
        'name': "mohamed",
        'age': 40,
        'image': static('students/images/3.jpeg')
    }
    ]
def index(request):
    return render(request, 'students/index.html', {'students': students})

def student_details(request, _id):
    
    item={}
    for student in students:
        
        if student['id'] == _id:
            item = student
            break
    return render(request, 'students/student_details.html', {'student': item})