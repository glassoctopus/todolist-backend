from django.db import models
from .character import Character

class EdgeOrFlaw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='edge_or_flaws')
    edge_or_flaw_name = models.CharField(max_length=69)
    description = models.CharField(max_length=666)
    bonus = models.DecimalField(max_digits=2, decimal_places=1)
    edge = models.BooleanField(False)
    flaw = models.BooleanField(False)
    
    def __str__(self):
        return self.edge_or_flaw_name