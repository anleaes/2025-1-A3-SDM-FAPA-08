from django.db import models
from inventories.models import Inventario
from items.models import Item

class InventoryItem(models.Model):
    inventory = models.ForeignKey(
        Inventario,
        on_delete=models.CASCADE,
        verbose_name='Inventario'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Item'
    )
    quantity = models.IntegerField('Quantidade', default=1)
    
    class Meta:
        verbose_name = 'Item do Inventario'
        verbose_name_plural = 'Itens do Inventario'
        ordering =['id']
    
    def __str__(self):
        return f"{self.quantity}x {self.item.nome} - {self.inventory}"
