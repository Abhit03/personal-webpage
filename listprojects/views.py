from django.shortcuts import render

from projects.models import Project
from tables.tables import ProjectsTable

# Create your views here.
def listprojects(request):
    """
    View to list all courses
    """
    context = {}

    cern_projects_list = Project.objects.filter(organisation="cern")
    cern_table = ProjectsTable(cern_projects_list)
    context["cern_table"] = cern_table

    sharedelectric_projects_list = Project.objects.filter(organisation="sharedElectric")
    sharedelectric_table = ProjectsTable(sharedelectric_projects_list)
    context["sharedelectric_table"] = sharedelectric_table

    heidelberg_projects_list = Project.objects.filter(organisation="heidelberg")
    heidelberg_table = ProjectsTable(heidelberg_projects_list)
    context["heidelberg_table"] = heidelberg_table

    return render(request, "listprojects/list.html", context)



