from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    senha = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if Usuario.objects.filter(nome=self.nome, senha=self.senha).exists():
            pass
        else:
            super(Usuario, self).save(*args, **kwargs)