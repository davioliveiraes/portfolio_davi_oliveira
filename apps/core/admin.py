from django.contrib import admin

from .models import Contact, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "technologies", "featured", "created_at")
    list_filter = ("featured", "created_at")
    search_fields = ("title", "description", "technologies")
    list_editable = ("featured",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "read", "created_at")
    list_filter = ("read", "created_at")
    search_fields = ("name", "email", "message")
    list_editable = ("read",)
    readonly_fields = ("name", "email", "message", "created_at")
