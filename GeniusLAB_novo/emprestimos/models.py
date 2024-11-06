from django.db import models
from django.conf import settings  # Para referenciar o modelo de usuário configurado
from GeniusLAB_novo.livros.models import Livro
from django.utils import timezone
from datetime import timedelta


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_prevista_devolucao = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)  # Atualizado quando o livro é devolvido

    def __str__(self):
        return f"Empréstimo de {self.livro} para {self.usuario.username}"

    def save(self, *args, **kwargs):
            if not self.pk:  # Se for um novo empréstimo
                if self.livro.disponivel:
                    self.livro.disponivel = False
                    self.livro.save()
                    self.data_prevista_devolucao = timezone.now() + timedelta(days=14)
                else:
                    raise ValueError("O livro não está disponível para empréstimo")
            else:  # Em caso de devolução
                if self.data_devolucao:
                    self.livro.disponivel = True
                    self.livro.save()
                    
            super().save(*args, **kwargs)