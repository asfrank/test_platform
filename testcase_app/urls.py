from django.urls import path

from testcase_app.views import TestcaseView, CaseDebugView, CaseAssertView, CaseSaveView

urlpatterns = [
    path('', TestcaseView.as_view(), name="testcase"),
    path('debug/', CaseDebugView.as_view(), name='casedebug'),
    path('assert/', CaseAssertView.as_view(), name='caseassert'),
    path('save_case/', CaseSaveView.as_view(), name='casesave'),
]