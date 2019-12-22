from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from module_app.models import Module
from module_app.forms import ModuleForm
from project_app.models import Project


class ModuleView(View):
    @method_decorator(login_required)
    def get(self, request):
        modules = Module.objects.all()
        return render(request, "module.html", {"modules": modules,
                                               "type": "list"})

class AddModuleView(View):
    @method_decorator(login_required)
    def get(self, request):
        module_form = ModuleForm()
        return render(request, "module.html", {"module_form": module_form,
                                               "type": "add"})

    @method_decorator(login_required)
    def post(self, request):
        module_form = ModuleForm(request.POST)
        if module_form.is_valid():
            project = module_form.cleaned_data['project']
            name = module_form.cleaned_data['name']
            describe = module_form.cleaned_data['describe']
            Module.objects.create(project=project, name=name, describe=describe)
            return HttpResponseRedirect('/module/')
        # return HttpResponseRedirect('/project/')

class EditModuleView(View):
    @method_decorator(login_required)
    def get(self, request, mid):
        if mid:
            module = Module.objects.get(id=mid)
            module_form = ModuleForm(instance=module)
            return render(request, "module.html", {"module_form": module_form,
                                                    "type": "edit",
                                                    "mid": mid})

    @method_decorator(login_required)
    def post(self, request, mid):
        module_form = ModuleForm(request.POST)
        if module_form.is_valid():
            module = Module.objects.get(id=mid)
            name = module_form.cleaned_data['name']
            describe = module_form.cleaned_data['describe']
            project = module_form.cleaned_data['project']
            module.name = name
            module.describe = describe
            module.project = project
            module.save()
            return HttpResponseRedirect('/module/')

class DeleteModuleView(View):
    @method_decorator(login_required)
    def get(self, request, mid):
        if mid:
            try:
                module = Module.objects.get(id=mid)
            except Module.DoesNotExist:
                return HttpResponseRedirect('/module/')
            else:
                module.delete()
            return HttpResponseRedirect('/module/')

class GetModuleListView(View):
    @method_decorator(login_required)
    def post(self, request):
        pid = request.POST.get('pid', '')
        if pid == "":
            return JsonResponse({"success": "false", "message": "项目id不能为空"})
        project = Project.objects.filter(id=pid)[0]
        modules = Module.objects.filter(project=project)
        module_list = []
        for module in modules:
            module_list.append({"name": module.name, "value": module.id})
        return JsonResponse({"success": "true", "message": "请求成功", "data": module_list})

    def get(self, request):
        return JsonResponse({"success": "false", "message": "请求方法错误"})




