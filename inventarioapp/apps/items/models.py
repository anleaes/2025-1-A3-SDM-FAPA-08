from django.db import models

class Item(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao')
    photo = models.ImageField('Foto', upload_to='photos', null=True, blank=True)
    doc = models.FileField('Documentos', upload_to='docs', null=True, blank=True)
    raridade = models.CharField('Raridade', max_length=50)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering =['id']
    
    def __str__(self):
        return self.nome
