from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)