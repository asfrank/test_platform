from django.urls import path

from project_app.views import ProjectView, EditProjectView, AddProjectView, DeleteProjectView

urlpatterns = [
    path('', ProjectView.as_view(), name="project"),
    path('add_project/', AddProjectView.as_view(), name="add_project"),
    path('edit_project/<int:pid>/', EditProjectView.as_view(), name="edit_project"),
    path('delete_project/<int:pid>/', DeleteProjectView.as_view(), name="delete_project"),
]