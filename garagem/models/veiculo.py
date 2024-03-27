from django.db import models

from garagem.models import Marca, Categoria, Cor


class Veiculo(models.Model):
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    def __str__(self):
        return f"{self.marca} {self.ano} | {self.cor}"
