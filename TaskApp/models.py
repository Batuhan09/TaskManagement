from django.db import models

# Create your models here.


class Tasks(models.Model):
    TaskId = models.AutoField(primary_key=True)
    TaskTitle = models.CharField(max_length=500)