from django.urls import path

from testcase_app.views import TestcaseView, CaseDebugView

urlpatterns = [
    path('', TestcaseView.as_view(), name="testcase"),
    path('debug/', CaseDebugView.as_view(), name='casedebug'),
]