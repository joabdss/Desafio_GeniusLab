from rest_framework import serializers
from .models import Emprestimo
from GeniusLAB_novo.livros.serializers import LivroSerializer
from usuario.serializers import UsuarioSerializer

class EmprestimoSerializer(serializers.ModelSerializer):
    livro = LivroSerializer(read_only=True)
    usuario = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Emprestimo
        fields = ['id', 'livro', 'usuario', 'data_emprestimo', 'data_prevista_devolucao', 'data_devolucao']