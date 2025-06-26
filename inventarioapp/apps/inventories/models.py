from django.db import models
from playerprofiles.models import PlayerProfile

class Inventario(models.Model):
    owner = models.ForeignKey(
        PlayerProfile,
        on_delete=models.CASCADE,
        verbose_name='Dono',
    )
    max_capacity = models.IntegerField('Capacidade Maxima', default=20)
    created_at = models.DateTimeField('Data de Criacao', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        ordering =['id']
    
    def __str__(self):
        return f"Inventario de {self.owner.playername}"
