from django.db import models
from .character import Character

class Health(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='healths')
    stun_level = models.IntegerField(default=0)
    wound_level = models.IntegerField(default=0)
    incapacitated = models.BooleanField(False)
    mortally_wounded = models.BooleanField(False)
    
    def __str__(self):
        return f"Health status for {self.character.name}"