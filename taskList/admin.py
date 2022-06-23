from django.contrib import admin
from .models import Frame, Task

# Register your models here.
@admin.register(Frame)
class AuthorAdmin(admin.ModelAdmin):
    list_display=("id", "title")

@admin.register(Task)
class AuthorAdmin(admin.ModelAdmin):
    list_display=("id", "title", "frame_id")