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
        header = request.POST.get("header", "") or "{}"
        param_type = request.POST.get("param_type", "")
        parameter = request.POST.get("parameter", "") or "{}"

        json_header = header.replace("\'", "\"")
        try:
            header = json.loads(json_header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        json_param = parameter.replace("\'", "\"")
        try:
            payload = json.loads(json_param)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        if method == "get":
            if header == "":
                r = requests.get(url=url, params=payload)
            else:
                r = requests.get(url=url, params=payload, headers=header)

        if method == "post":
            if param_type == "form":
                if header == "":
                    r = requests.post(url, data=payload)
                else:
                    r = requests.post(url, data=payload, headers=header)

            if param_type == "json":
                if header == "":
                    r = requests.post(url, json=payload)
                else:
                    r = requests.post(url, json=payload, headers=header)
        return JsonResponse({"result": r.text})

class CaseAssertView(View):
    @method_decorator(login_required)
    def post(self, request):
        result_text = request.POST.get('result', '')
        assert_text = request.POST.get('assert', '')
        assert_method = request.POST.get('assert_method', '')
        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})
        if assert_method == "contains":
            if assert_text not in result_text:
                return JsonResponse({"result": "断言失败"})
            return JsonResponse({"result": "断言成功"})
        if assert_method == "equals":
            if assert_text == result_text:
                return JsonResponse({"result": "断言成功"})
            return JsonResponse({"result": "断言失败"})




