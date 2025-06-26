from django.db import models
from apps.users.models import User

class PlayerProfile(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuario',
    )
    level = models.IntegerField('Nivel', default=1)
    experience = models.IntegerField('Experiencia', default=0)
    total_score = models.IntegerField('Pontuacao Total', default=0)
    
