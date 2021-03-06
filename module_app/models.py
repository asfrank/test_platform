from django.db import models

from project_app.models import Project


class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="所属项目")
    name = models.CharField(max_length=50, verbose_name="名称")
    describe = models.TextField(default="", verbose_name="描述")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name