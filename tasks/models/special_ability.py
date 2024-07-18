from django.db import models
from .character import Character

class SpecialAbility(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='special_abilities')
    special_ability_name = models.CharField(max_length=26)
    special_ability_description = models.CharField(max_length=666)
    special_ability_notes = models.CharField(max_length=666)
    special_ability_code = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.special_ability_name