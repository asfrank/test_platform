from django.urls import path

from testcase_app.views import TestcaseView, CaseDebugView, CaseAssertView, CaseSaveView, CaseAddView, CaseEditView, CaseDeleteView, GetCaseInfoView

urlpatterns = [
    path('', TestcaseView.as_view(), name="testcase"),
    path('add_case/', CaseAddView.as_view(), name="caseadd"),
    path('edit_case/<int:cid>/', CaseEditView.as_view(), name="caseadd"),
    path('delete_case/', CaseDeleteView.as_view(), name="caseadd"),

    path('debug/', CaseDebugView.as_view(), name='casedebug'),
    path('assert/', CaseAssertView.as_view(), name='caseassert'),
    path('save_case/', CaseSaveView.as_view(), name='casesave'),
    path('get_case_info/', GetCaseInfoView.as_view(), name='getcaseinfo')
]