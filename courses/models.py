from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Course(models.Model):
    SUBJECT_CHOICES = (
        ("physics", "Physics"),
        ("math", "Mathematics"),
        ("cs", "Computer Science"),
        ("electronics", "Electronics"),
        ("stats", "Statistics"),
        ("philosophy", "Philosophy"),
        ("arts", "Arts"),
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

    COURSE_LEVEL_CHOICES = (
        ("others", "Others"),
        ("bachelors", "Bachelors"),
        ("masters", "Masters"),
    )

    GRADE_ALPHABET_CHOICES = (
        ("a", "A"),
        ("a-", "A-"),
        ("b+", "B+"),
        ("b", "B"),
        ("c", "C"),
    )

    name = models.CharField(max_length=100)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=25)
    coursetype = models.CharField(choices=COURSE_TYPE, max_length=25)
    credits = models.PositiveIntegerField(null=True)
    grade = models.FloatField(null=True)
    gradealphabet = models.CharField(choices=GRADE_ALPHABET_CHOICES, max_length=5, null=True)
    gradescale = models.CharField(choices=GRADESCALE_CHOICES, max_length=50, blank=True)
    description = models.TextField(blank = True)
    comment = models.TextField(blank = True)
    externallinks = models.TextField(blank = True)
    courselevel = models.CharField(max_length=25, choices=COURSE_LEVEL_CHOICES, null=True)
    semester = models.PositiveSmallIntegerField(null=True, blank = True)

    def __str__(self):
        return "{}".format(self.name)