from django.db import models
from .character import Character

class Possession(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='possessions')
    possession_name = models.CharField(max_length=69)
    description = models.CharField(max_length=666)
    possession_note = models.CharField(max_length=666)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.possession_name