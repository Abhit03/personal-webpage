from django.http import HttpResponseRedirect
from django.shortcuts import render

from courses.models import Course
from tables.tables import MastersCourseTable, BachelorsCourseTable

# Create your views here.
def listcourses(request):
    """
    View to list all courses
    """
    context = {}

    masters_course_list = Course.objects.filter(courselevel="masters")
    masters_table = MastersCourseTable(masters_course_list)
    context["masters_table"] = masters_table

    bachelors_course_list = Course.objects.filter(courselevel="bachelors")
    bachelors_table = BachelorsCourseTable(bachelors_course_list)
    context["bachelors_table"] = bachelors_table

    return render(request, "listcourses/list.html", context)



