from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from personal.models import Project


class ProjectView(View):
    @method_decorator(login_required)
    def get(self, request):
        project_all = Project.objects.all()
        return render(request, "project.html", {"projects": project_all,
                                                "type": "list"})


class AddProjectView(View):
    """
    添加项目
    """
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "project.html", {"type": "add"})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        if name == "":
            return render(request, "project.html", {"type": "add", "name_error": "项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect('/project/')

class EditProjectView(View):
    """
    编辑项目
    """
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "project.html", {"type": "edit"})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        if name == "":
            return render(request, "project.html", {"type": "edit", "name_error": "项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect('/project/')


