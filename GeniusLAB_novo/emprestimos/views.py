from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Emprestimo
from .serializers import Emprestimo
from livros.models import Livro

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        # Custom logic to ensure the book is available
        livro = serializer.validated_data['livro']
        if livro.disponivel:
            livro.disponivel = False  # Marca o livro como indisponível
            livro.save()
            serializer.save()
        else:
            raise serializers.ValidationError("O livro não está disponível para empréstimo")