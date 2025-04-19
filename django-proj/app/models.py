from django.db import models

class Quote(models.Model):
    contractor_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    roof_size = models.IntegerField(default=0)
    roof_type = models.CharField(max_length=200)
    project_city = models.CharField(max_length=200)
    project_state = models.CharField(max_length=200)
    project_date = models.DateTimeField("project-date")
