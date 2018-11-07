from django.db import models

class caseoverview(models.Model):
    caseid = models.CharField(max_length=20)
    title = models.CharField(max_length=125)
    owner = models.CharField(max_length=125)
    catagory = models.CharField(max_length=20)
    subcatagory = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    progress = models.CharField(max_length=100)
    progressDetails = models.TextField()
    incidentReporter = models.CharField(max_length=50)
    incidentOwner = models.CharField(max_length=50)
    priority = models.CharField(max_length=10)
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.caseid} {self.title}'



# Create your models here.
