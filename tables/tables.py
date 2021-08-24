import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from tables.utilities.utilities import render_grade_color, render_gradealphabet_color

# from tables.utilities.utilities import (
#     render_component,
# )

from courses.models import Course
from projects.models import Project


class MastersCourseTable(tables.Table):
    """
    Simple readonly table listing all the courses with Grades
    """

    name = tables.Column(verbose_name = "Course Name")
    grade = tables.Column()
    subject = tables.Column()
    description = tables.Column()

    class Meta:
        model = Course
        fields = ()
        attrs = {"class": "table table-hover table-bordered table-fixed"}

    def render_description(self, value):
        value_list = value.split(",")
        li_tags = ''
        for item in value_list:
            li_tags += '<li>{}</li>'.format(item)
        return mark_safe(
            '<ul>'
            '{}'
            '</ul>'.format(li_tags)
        )

    def render_grade(self, value):
        return render_grade_color(value)

class BachelorsCourseTable(tables.Table):
    """
    Simple readonly table listing all the courses with Grades
    """

    name = tables.Column(verbose_name = "Course Name")
    gradealphabet = tables.Column(verbose_name = "Grade")
    subject = tables.Column()

    class Meta:
        model = Course
        fields = ()
        attrs = {"class": "table table-hover table-bordered table-fixed"}

    def render_gradealphabet(self, value):
        return render_gradealphabet_color(value)

class OthersCourseTable(tables.Table):
    """
    Simple readonly table listing online courses
    """

    name = tables.Column(verbose_name = "Course Name")
    comment = tables.Column(verbose_name = "Platform")
    description = tables.Column(verbose_name = "Offered by")
    externallinks = tables.Column(verbose_name = "Links")

    class Meta:
        model = Course
        fields = ()
        attrs = {"class": "table table-hover table-bordered table-fixed"}

    def render_externallinks(self, value):
        return format_html(
            '<a href="{}">'
            'Certificate'
            '</a>', value)

class ProjectsTable(tables.Table):
    """
    Simple readonly table listing completed rpoject
    """

    name = tables.Column(verbose_name = "Project Name")
    duration = tables.Column()
    languages = tables.Column(verbose_name = "Languages & Frameworks")
    description = tables.Column(verbose_name = "Short description")
    applink = tables.Column(verbose_name = "Application link")
    codebase = tables.Column()
    
    class Meta:
        model = Project
        fields = ()
        attrs = {"class": "table table-hover table-bordered table-fixed"}

    def render_codebase(self, value):
        return format_html(
            '<a href="{}">'
            'Github'
            '</a>', value)