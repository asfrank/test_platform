from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="项目名")
    describe = models.TextField(default="", verbose_name="描述")
    status = models.BooleanField(default=1, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name
