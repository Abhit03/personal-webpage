from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Course(models.Model):
    SUBJECT_CHOICES = (
        ("physics", "Physics"),
        ("math", "Mathematics"),
        ("cs", "Informatics"),
        ("electronics", "Electronics"),
    )

    COURSE_TYPE = (
        ("lecture", "Lecture"),
        ("seminar", "Seminar"),
        ("practical", "Practical"),
    )

    GRADESCALE_CHOICES = (
        ("german", "Best: 1.0; Worst: 5.0"),
        ("100scale", "Best: 100; Worst: 0"),
        ("50scale", "Best: 50; Worst: 0"),
    )

    name = models.CharField(max_length=50)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=25)
    coursetype = models.CharField(choices=COURSE_TYPE, max_length=25)
    credits = models.PositiveIntegerField(null=True)
    grade = models.FloatField(null=True)
    gradescale = models.CharField(choices=GRADESCALE_CHOICES, max_length=50)
    description = models.TextField(blank = True)
    comment = models.TextField(blank = True)
    externallinks = models.TextField(blank = True)

    def __str__(self):
        return "{}".format(self.name)