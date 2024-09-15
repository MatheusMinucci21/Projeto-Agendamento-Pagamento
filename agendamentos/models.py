from django.db import models
from django.db.models import IntegerField


# Criação da estrutura do banco de dados
class agendamentopagamento(models.Model):
    data_pagamento=models.DateField()
    permite_recorrencia=models.BooleanField(default=False)
    quantidade_recorrencia=models.IntegerField()
    intervalo_recorrencia=models.IntegerField()
    status_ocorrencia=models.CharField(max_length=30)
    agencia=models.IntegerField()
    conta=models.IntegerField()
    valor_pagamento=models.DecimalField(max_digits=6,decimal_places=2)


