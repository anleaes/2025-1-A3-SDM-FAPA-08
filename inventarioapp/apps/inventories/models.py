from django.db import models
from playerprofiles.models import PlayerProfile

class Inventario(models.Model):
    dono = models.ForeignKey(
        PlayerProfile,
        on_delete=models.CASCADE,
        verbose_name='Dono',
        related_name='inventarios'
    )
    capacidade_maxima = models.IntegerField('Capacidade Maxima', default=20)
    data_criacao = models.DateTimeField('Data de Criacao', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering =['id']
    
    def __str__(self):
        return f"Inventario de {self.dono.playername}"
