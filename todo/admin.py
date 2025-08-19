from django.contrib import admin
from .models import Category, Todo


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "created_at", "updated_at"]
    search_fields = ["title"]
    ordering = ["-created_at"]
    
admin.site.register(Category, CategoryAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "description","category","is_active", "completed", "created_at", "updated_at"]
    search_fields = ["title", "description"]
    list_filter = ["is_active", "completed", "created_at"]
    ordering = ["-created_at"]
    
admin.site.register(Todo, TodoAdmin)