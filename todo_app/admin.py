from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TaskToDo


# Register your models here.
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('task','is_completed','updated_at')
#     search_fields = ('task',)
#     list_editable = ('is_completed',)
    
class TaskAdminToDo(admin.ModelAdmin):
    list_display = ('id','name','task','priority','is_completed','updated_at')
    list_display_links = ('id','name','task',)
    search_fields = ('task',)
    list_editable = ('is_completed',)
    



# admin.site.register(Task,TaskAdmin)
admin.site.register(TaskToDo,TaskAdminToDo)