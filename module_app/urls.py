from django.urls import path

from module_app.views import ModuleView, EditModuleView, AddModuleView, DeleteModuleView

urlpatterns = [
    path('', ModuleView.as_view(), name="module"),
    path('add_module/', AddModuleView.as_view(), name="add_module"),
    path('edit_module/<int:mid>/', EditModuleView.as_view(), name="edit_module"),
    path('delete_module/<int:mid>/', DeleteModuleView.as_view(), name="delete_module"),
]