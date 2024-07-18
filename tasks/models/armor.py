from django.db import models
from .character import Character

class Armor(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='armors')
    armor_name = models.CharField(max_length=23)
    strength_bonus = models.DecimalField(max_digits=2, decimal_places=1)
    dexterity_penalty = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.armor_name