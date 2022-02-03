from django.db import models

# Create your models here.

class Artigo(models.Model):
    processo = models.CharField(max_length=500)
    assunto = models.TextField()
    responsavel = models.CharField(max_length=500)
    relator = models.CharField(max_length=500)
    interesado = models.CharField(max_length=500)
    dispositivo = models.TextField()
    nome = models.CharField(max_length=500)

class Palavra(models.Model):
    FKArtigoId = models.ForeignKey(Artigo, on_delete=models.CASCADE, null=True, related_name='artigoPalavra')
    Palavra = models.CharField(max_length=600)
    