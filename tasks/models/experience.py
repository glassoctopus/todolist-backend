import datetime
from django.db import models
from .character import Character

class Experience(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='experiences')
    adventure = models.CharField(max_length=666)
    xp_gained = models.IntegerField(default=0)
    earth_date = models.DateField(default=datetime.date(2024, 6, 11))
    
    def __str__(self):
        return self.adventure