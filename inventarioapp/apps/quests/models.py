from django.db import models

class Quest(models.Model):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descricao')
    xp_reward = models.IntegerField('Recompensa XP', default=0)
    
    class Meta:
        verbose_name = 'Missao'
        verbose_name_plural = 'Missoes'
        ordering =['id']
    
    def __str__(self):
        return self.title
