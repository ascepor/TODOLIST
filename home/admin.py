from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import *  
from.Serializers import *


# Register your models here.

class ToDoAdmin(UserAdmin):
    list_display = ToDo.DisplayFields
    filter_horizontal = ()
    list_filter = ToDo.FilterFields
    ordering = ('Tag',)
    fieldsets = ()
 
   



admin.site.register(ToDo, ToDoAdmin)