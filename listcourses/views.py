from django.http import HttpResponseRedirect
from django.shortcuts import render

from courses.models import Course
from tables.tables import MastersCourseTable

# Create your views here.
def listcourses(request):
    """
    View to list all courses
    """
    context = {}
    course_list = Course.objects.all()
    masters_table = MastersCourseTable(course_list)

    context["masters_table"] = masters_table
    return render(request, "listcourses/list.html", context)



