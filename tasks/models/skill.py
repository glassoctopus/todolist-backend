from django.db import models
from .character import Character

class Skill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='skills')
    attribute = models.CharField(max_length=26)
    skill_name = models.CharField(max_length=26)
    skill_code = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return f"{self.skill_name} (code {self.skill_code})"
