from django.db import models

class Achievement(models.Model):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descricao')
    points = models.IntegerField('Pontos', default=0)
    
    class Meta:
        verbose_name = 'Conquista'
        verbose_name_plural = 'Conquistas'
        ordering =['id']
    
    def __str__(self):
        return self.title
