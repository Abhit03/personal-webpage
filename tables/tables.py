import django_tables2 as tables
from django.utils.safestring import mark_safe
from tables.utilities.utilities import render_grade_color, render_gradealphabet_color

# from tables.utilities.utilities import (
#     render_component,
# )

from courses.models import Course


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