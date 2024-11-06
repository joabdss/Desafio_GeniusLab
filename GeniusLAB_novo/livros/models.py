from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True) # livro disponivel

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
