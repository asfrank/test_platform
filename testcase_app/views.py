from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.http import JsonResponse

import requests
import json

class TestcaseView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'testcase.html', {"type": "debug"})


class CaseDebugView(View):
    @method_decorator(login_required)
    def post(self, request):
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        param_type = request.POST.get("param_type", "")
        parameter = request.POST.get("parameter", "")
        if parameter:
            parameter = json.loads(parameter)

        if method == "get":
            r = requests.get(url=url)
            return JsonResponse({"result": r.text})
        return JsonResponse({"result": "ok"})

