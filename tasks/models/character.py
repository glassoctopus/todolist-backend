from django.db import models
from .archetype import Archetype

class Character(models.Model):
    uid = models.CharField(max_length=113)
    image = models.CharField(max_length=223)
    name = models.CharField(max_length=69)
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE, related_name='archetypes')
    species = models.CharField(max_length=69)
    homeworld = models.CharField(max_length=69)
    gender = models.CharField(max_length=13)
    age = models.IntegerField(default=21)
    height = models.CharField(max_length=13)
    weight = models.CharField(max_length=13)
    physical_description = models.CharField(max_length=1369)
    personality = models.CharField(max_length=1369)
    background = models.CharField(max_length=1369)
    objectives = models.CharField(max_length=1369)
    a_quote = models.CharField(max_length=1369)
    credits = models.IntegerField(default=0)
    force_sensitive = models.BooleanField(default=False)
    dexiterity = models.DecimalField(max_digits=2, decimal_places=2)
    knowledge = models.DecimalField(max_digits=2, decimal_places=2)
    mechanical = models.DecimalField(max_digits=2, decimal_places=2)
    perception = models.DecimalField(max_digits=2, decimal_places=2)
    strength = models.DecimalField(max_digits=2, decimal_places=2)
    technical = models.DecimalField(max_digits=2, decimal_places=2)
    force_control = models.DecimalField(max_digits=2, decimal_places=2)
    force_sense = models.DecimalField(max_digits=2, decimal_places=2)
    force_alter = models.DecimalField(max_digits=2, decimal_places=2)
    force_points = models.DecimalField(max_digits=2, decimal_places=1)
    dark_side_points = models.DecimalField(max_digits=2, decimal_places=1)
    force_strength = models.DecimalField(max_digits=2, decimal_places=1)
    
    
    def __str__(self):
        return self.name

