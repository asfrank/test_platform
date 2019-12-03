from django.db import models

from personal.models.project import Project


class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    describe = models.TextField(default="")
    create_time = models.DateTimeField(auto_now_add=True)