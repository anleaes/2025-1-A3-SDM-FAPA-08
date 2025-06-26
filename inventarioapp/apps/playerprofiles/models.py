from django.db import models
from users.models import User

class PlayerProfile(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Usuario',
    )
    level = models.IntegerField('Nivel', default=1)
    experience = models.IntegerField('Experiencia', default=0)
    total_score = models.IntegerField('Pontuacao Total', default=0)

    class Meta:
        verbose_name = 'Perfil de Jogador'
        verbose_name_plural = 'Perfis de Jogadores'
        ordering = ['id']
    
    def __str__(self):
        return f"{self.user.username} - Level {self.level}"