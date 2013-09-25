from django.db import models

class rawMatLists(models.Model):
    listName = models.CharField(max_length=15)
    forColor = models.CharField(max_length=15)

    def createList(self, list_name, color_name):
        self.listName = list_name
        self.forColor = color_name
        self.save()
        return self

class rawMat(models.Model):
    name = models.CharField(max_length=40)
    rawMatList = models.ManyToManyField(rawMatLists)

    def createRawMat(self, name):
        self.name = name
        return self

    def addList(self, list_name):
        self.rawMatList.add(list_name)
