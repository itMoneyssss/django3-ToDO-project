from django.contrib import admin
from .models import Todo


class ToDoAdmin(admin.ModelAdmin):
    readonly_fields = ['data_of_created']


admin.site.register(Todo, ToDoAdmin)
