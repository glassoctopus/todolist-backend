from django.db import models
from .character import Character
from .equipment import Equipment

class CharacterEquipment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_equipment')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.character.name} - {self.equipment.equipment_name} x {self.quantity}"