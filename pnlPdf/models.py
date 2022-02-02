from django.db import models

# Create your models here.

class Artigo(models.Model):
    Artgo = models.CharField(max_length=500)

class Sentenca(models.Model):
    FkArtigoId = models.ForeignKey(Artigo, on_delete=models.CASCADE, null=True, related_name='artigoSentenca')
    Sentenca= models.CharField(max_length=1200)

class Palavra(models.Model):
    FKArtigoId = models.ForeignKey(Artigo, on_delete=models.CASCADE, null=True, related_name='artigoPalavra')
    Palavra = models.CharField(max_length=200)
    