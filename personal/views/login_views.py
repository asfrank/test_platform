from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.contrib import auth

from personal.models.project import Project

class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {
                "error": "用户名或密码为空"
            })
        user = auth.authenticate(username=username, password= password)
        if user is None:
            return render(request, "index.html", {
                "error": "用户名或密码错误"
            })

        auth.login(request, user)
        return HttpResponseRedirect("/project")

class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect("/")




