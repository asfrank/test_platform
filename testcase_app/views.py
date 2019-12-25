from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.http import JsonResponse

import requests
import json

from testcase_app.models import TestCase


class TestcaseView(View):
    '''
    用例列表
    '''
    @method_decorator(login_required)
    def get(self, request):
        cases = TestCase.objects.all()
        return render(request, 'case_list.html', {"cases": cases})

class CaseAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'case_add.html')

class CaseEditView(View):
    @method_decorator(login_required)
    def get(self, request, cid):
        # case_info = TestCase.objects.filter(id=cid)[0]
        return render(request, 'case_edit.html')

class CaseDeleteView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'case_add.html')

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


class CaseSaveView(View):
    '''
    用例保存
    '''

    @method_decorator(login_required)
    def post(self, request):
        url = request.POST.get('url', '')
        method = request.POST.get('method', '')
        header = request.POST.get('header', '')
        parameter_type = request.POST.get('par_type', '')
        parameter_body = request.POST.get('par_body', '')
        assert_type = request.POST.get('ass_type', '')
        assert_text = request.POST.get('ass_text', '')
        module_id = request.POST.get('mid', '')
        name = request.POST.get('name', '')
        if name == "":
            return JsonResponse({"success": "false", "message": "用例名称不能为空"})

        if module_id == "":
            return JsonResponse({"success": "false", "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"success": "false", "message": "断言的类型或文本不能为空"})

        if method == "get":
            module_number = 1
        elif method == "post":
            module_number = 2
        elif method == "put":
            module_number = 3
        elif method == "delete":
            module_number = 4
        else:
            return JsonResponse({"success": "false", "status": 10104, "message": "未知的请求方法"})

        if parameter_type == "form":
            parameter_number = 1
        elif parameter_type == "json":
            parameter_number = 2
        else:
            return JsonResponse({"success": "false", "status": 10104, "message": "未知的参数类型"})

        if assert_type == "equals":
            assert_number = 1
        elif assert_type == "contains":
            assert_number = 2
        else:
            return JsonResponse({"success": "false", "status": 10104, "message": "未知的断言类型"})

        TestCase.objects.create(name=name, module_id=module_id,
                                url=url, method=module_number, header=header,
                                param_type=parameter_number, param=parameter_body,
                                assert_type=assert_number, assert_text=assert_text)
        return JsonResponse({"success": "true", "message": "创建成功！"})

    def get(self, request):
        return JsonResponse({"success": "false", "message": "请求方法错误"})

class GetCaseInfoView(View):
    '''
    获取接口数据
    '''
    @method_decorator(login_required)
    def post(self, request):
        cid = request.POST.get('cid', '')
        case = TestCase.objects.filter(id=cid)[0]
        case_dict = {
            "id": case.id,
            "url": case.url,
            "name": case.name,
        }
        return JsonResponse({"success": "true", "message": "请求成功！", "data": case_dict})

    @method_decorator(login_required)
    def get(self, request):
        return JsonResponse({"success": "false", "message": "请求方法错误"})
