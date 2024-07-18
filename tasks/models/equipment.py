from django.db import models

class Equipment(models.Model):
    equipment_name = models.CharField(max_length=269)
    equipment_category = models.CharField(max_length=269)
    equipment_sub_category = models.CharField(max_length=269, null=True, blank=True)
    equipment_model = models.CharField(max_length=269, null=True, blank=True)
    equipment_type = models.CharField(max_length=113, null=True, blank=True)
    equipment_scale = models.CharField(max_length=113, null=True, blank=True)
    equipment_cost = models.IntegerField(default=0)
    equipment_description = models.CharField(max_length=1369, null=True, blank=True)
    equipment_availability = models.CharField(max_length=26, null=True, blank=True)
    equipment_skill = models.CharField(max_length=113, null=True, blank=True)
    equipment_damage = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    equipment_ammo = models.IntegerField(default=0, null=True, blank=True)
    equipment_charges = models.IntegerField(default=0, null=True, blank=True)
    equipment_uses = models.IntegerField(default=0, null=True, blank=True)
    equipment_use_notes = models.CharField(max_length=3666, null=True, blank=True)
    source = models.CharField(max_length=1369, null=True, blank=True)
    
    def __str__(self):
        return f"{self.equipment_name} (Model: {self.equipment_model}, Type: {self.equipment_type})"
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"