from django.db import models

from module_app.models import Module


class TestCase(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="所属模块")
    name = models.CharField(max_length=50, verbose_name="名称")
    url = models.TextField(verbose_name="URL")
    method = models.SmallIntegerField(verbose_name="请求方法")  #1get 2post
    header = models.TextField(verbose_name="请求头")
    param_type = models.SmallIntegerField(verbose_name="参数类型") #1form 2json
    param = models.TextField(verbose_name="参数内容")
    assert_type = models.SmallIntegerField(verbose_name="断言类型") #1相等 2包含
    assert_text = models.TextField(verbose_name="断言内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name