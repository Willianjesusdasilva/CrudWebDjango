from django.db import models


class cliente(models.Model):

    idcliente = models.AutoField(primary_key=True)
    nmcliente = models.CharField('Cliente',max_length=100)
    dtnascimento = models.DateTimeField('Data de Nascimento')
    dtcoleta = models.DateTimeField('Data da Coleta')
    dtentrega = models.DateTimeField('Data de Entrega')
    nmmedico =  models.CharField('Médico responsável',max_length=100)

    def __str__(self):
        return self.nmcliente
