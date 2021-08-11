from django.http import HttpResponseRedirect
from django.shortcuts import render

from courses.models import Course
from tables.tables import CourseTable

# Create your views here.
def listcourses(request):
    """
    View to list all courses
    """
    context = {}
    course_list = Course.objects.all()
    table = CourseTable(course_list)

    context["table"] = table
    return render(request, "listcourses/list.html", context)



