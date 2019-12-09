from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from personal.models import Project


class ProjectView(View):
    @method_decorator(login_required)
    def get(self, request):
        project_all = Project.objects.all()
        return render(request, "project.html", {"projects": project_all,
                                                "type": "list"})


class AddProjectView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "project.html", {"type": "add"})
