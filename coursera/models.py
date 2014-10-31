from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ": " + self.group