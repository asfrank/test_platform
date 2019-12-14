from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from personal.models import Project
from personal.forms import ProjectForm


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
    def get(self, request, pid):
        if pid:
            project = Project.objects.get(id=pid)
            form = ProjectForm(instance=project)
            return render(request, "project.html", {"type": "edit",
                                                    "project_form": form,
                                                    "pid": pid})

    @method_decorator(login_required)
    def post(self, request, pid):
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            project = Project.objects.get(id=pid)
            project.name = name
            project.describe = describe
            project.status = status
            project.save()
            return HttpResponseRedirect('/project/')



