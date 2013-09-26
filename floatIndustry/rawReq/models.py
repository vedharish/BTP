from django.db import models

class rawMatLists(models.Model):
    listName = models.CharField(max_length=15)
    forColor = models.CharField(max_length=15)
    currentCapacity = models.DecimalField(max_digits=7, decimal_places=3)

class rawMat(models.Model):
    name = models.CharField(max_length=40)
    rawMatList = models.ManyToManyField(rawMatLists)

class rawMatAttrib(models.Model):
    rawMatList = models.ForeignKey(rawMatLists)
    rawMat = models.ForeignKey(rawMat)
    quantity = models.DecimalField(max_digits=7, decimal_places=3)
