from django.shortcuts import render
from rest_framework import viewsets
from .models import Livro
from .serializers import Livro
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers

    # Permissao de que apenas usuarios auten. vejam livros, e que adm possam criar/edit
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()