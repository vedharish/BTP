from django.db import models

class rawMatLists(models.Model):
    listName = models.CharField(max_length=15)
    forColor = models.CharField(max_length=15)

class rawMat(models.Model):
    name = models.CharField(max_length=40)
    rawMatList = models.ManyToManyField(rawMatLists)
