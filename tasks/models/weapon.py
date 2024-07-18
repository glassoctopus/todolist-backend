from django.db import models
from .character import Character

class Weapon(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='weapons')
    weapon_name = models.CharField(max_length=23)
    attack_range = models.IntegerField(default=1)
    damage = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.weapon_name