from django.db import models

class Plano(models.Model):
    id_usuario = models.CharField(max_length=36, primary_key=False)  # Mude para CharField
    id_plano = models.IntegerField(null=True)
    id_design = models.IntegerField(null=True)
    nome_1 = models.CharField(max_length=100)
    nome_2 = models.CharField(max_length=100)
    data = models.DateField(null=True)
    convidados = models.IntegerField(default=50)

    decoracao = models.CharField(max_length=15)
    buffet = models.CharField(max_length=15)
    items_cerimonia = models.CharField(max_length=15)
    flores = models.CharField(max_length=15)
    transporte = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not Plano.objects.filter(id_usuario=self.id_usuario, nome_1=self.nome_1, nome_2=self.nome_2).exists():
            super(Plano, self).save(*args, **kwargs)