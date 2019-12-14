"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personal.views.login_views import LoginView, IndexView, LogoutView
from personal.views import project_views
from personal.views import module_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('project/', project_views.ProjectView.as_view(), name="project"),
    path('project/add_project/', project_views.AddProjectView.as_view(), name="add_project"),
    path('project/edit_project/<int:pid>/', project_views.EditProjectView.as_view(), name="edit_project"),
    path('module/', module_views.ModuleView.as_view(), name="module"),
]
