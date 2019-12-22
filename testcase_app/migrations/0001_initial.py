# Generated by Django 2.2 on 2019-12-22 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('url', models.TextField(verbose_name='URL')),
                ('method', models.SmallIntegerField(verbose_name='请求方法')),
                ('header', models.TextField(verbose_name='请求头')),
                ('param_type', models.SmallIntegerField(verbose_name='参数类型')),
                ('param', models.TextField(verbose_name='参数内容')),
                ('result', models.TextField(verbose_name='返回结果')),
                ('assert_type', models.SmallIntegerField(verbose_name='断言类型')),
                ('assert_text', models.TextField(verbose_name='断言内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_app.Module', verbose_name='所属模块')),
            ],
        ),
    ]
