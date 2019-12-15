from django.contrib import admin

from module_app.models import Module



class ModuleAdmin(admin.ModelAdmin):
    list_display = ["name", "describe", "create_time", "project"]

admin.site.register(Module, ModuleAdmin)
