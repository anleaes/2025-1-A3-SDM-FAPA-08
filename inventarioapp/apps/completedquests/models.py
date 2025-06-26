from django.db import models
from playerprofiles.models import PlayerProfile
from quests.models import Quest

class CompletedQuest(models.Model):
    player_profile = models.ForeignKey(
        PlayerProfile,
        on_delete=models.CASCADE,
        verbose_name='Perfil do Jogador',
    )
    quest = models.ForeignKey(
        Quest,
        on_delete=models.CASCADE,
        verbose_name='Missao'
    )
    completion_date = models.DateTimeField('Data de Conclusao', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Missao Concluida'
        verbose_name_plural = 'Missoes Concluidas'
        ordering =['id']
    
    def __str__(self):
        return f"{self.player_profile.playername} - {self.quest.title}"
