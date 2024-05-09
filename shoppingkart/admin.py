from django.contrib import admin
from .models import Category
class categoryadmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at' ,'updated_at','deleted_at')
    def has_change_permission(self, request, obj=None):
        return False
admin.site.register(Category)