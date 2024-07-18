from django.db import models
from .character import Character

class Note(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='notes')
    note = models.CharField(max_length=1369)
    
    def __str__(self):
        return self.note