from django.db import models

class Usuario(models.Model):
    username = models.CharField('Nome de Usuario', max_length=150, unique=True)
    email = models.EmailField('Email', unique=True)
    birth_date = models.DateField('Data de Nascimento', null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.username
