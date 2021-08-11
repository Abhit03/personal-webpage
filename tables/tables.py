import django_tables2 as tables
from django.utils.safestring import mark_safe

# from tables.utilities.utilities import (
#     render_component,
# )

from courses.models import Course


class CourseTable(tables.Table):
    """
    Simple readonly table listing all the courses with Grades
    """

    name = tables.Column(verbose_name = "Course Name")
    grade = tables.Column()
    gradescale = tables.Column()
    coursetype = tables.Column()
    description = tables.Column()
    comment = tables.TemplateColumn(
        '<div id="id_comment">'
            '{{record.comment}}'
        '</div>',
    )
    externallinks = tables.Column()

    class Meta:
        model = Course
        fields = ()
        attrs = {"class": "table table-hover table-bordered table-fixed"}






