import django_tables2 as tables
from django.utils.safestring import mark_safe

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
    description = tables.TemplateColumn(
        '<div id="id_comment">'
            '{{record.comment}}'
        '</div>',
    )

    class Meta:
        model = Course
        fields = ()
        attrs = {"class": "table table-hover table-bordered table-fixed"}






