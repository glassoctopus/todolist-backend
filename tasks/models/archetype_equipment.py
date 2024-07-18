from django.db import models
from .archetype import Archetype
from .equipment import Equipment

class ArchetypeEquipment(models.Model):
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE, related_name='archhetype_equipment')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.archetype.archetype_name} - {self.equipment.equipment_name} x {self.quantity}"