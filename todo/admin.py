from django.contrib import admin
from .models import Todo


# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "is_active", "completed", "created_at", "updated_at"]
    search_fields = ["title", "description"]
    list_filter = ["is_active", "completed", "created_at"]
    ordering = ["-created_at"]
    
admin.site.register(Todo, TodoAdmin)