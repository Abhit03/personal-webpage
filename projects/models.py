from django.db import models

# Create your models here.
class Project(models.Model):
    ORG_NAME = (
        ("sharedElectric", "Shared Electric GmbH"),
        ("cern", "CMS-CERN"),
        ("heidelberg", "Heidelberg University"),
        ("personal", "Personal projects"),
    )

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank = True)
    organisation = models.CharField(max_length=50, choices=ORG_NAME)
    duration = models.SmallIntegerField(null=True, blank = True)
    languages = models.TextField(blank = True)
    tools = models.TextField(blank = True)
    description = models.TextField(blank = True)
    comment = models.TextField(blank = True)
    codebase = models.TextField(blank = True)
    applink = models.TextField(blank = True)
    startdate = models.DateField(blank = True, null=True)
    enddate = models.DateField(blank = True, null=True)

    def __str__(self):
        return "{}".format(self.name)