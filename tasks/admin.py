from django.contrib import admin

from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_name', 'equipment_category', 'equipment_model', 'equipment_type')
    search_fields = ('equipment_name', 'equipment_category', 'equipment_model', 'equipment_type')
