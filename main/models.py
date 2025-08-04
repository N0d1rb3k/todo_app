from django.db import models

class Tododb(models.Model):
    title = models.CharField(max_length=30)
    task = models.CharField(max_length=4096)
    date = models.DateTimeField()

    def __str__(self):
        return self.title