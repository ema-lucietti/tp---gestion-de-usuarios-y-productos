from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Producto, Categoria
from usuarios.models import Usuario

class ProductoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Crear un usuario para pruebas
        self.user = Usuario.objects.create_user(
            username='testuser', 
            password='securepassword123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)
        
        # Crear una categoría
        self.categoria = Categoria.objects.create(
            nombre='Test Categoria',
            descripcion='Descripción de prueba'
        )
        
        self.producto_data = {
            'nombre': 'Test Producto',
            'descripcion': 'Descripción de prueba',
            'precio': '99.99',
            'stock': 10,
            'categoria': self.categoria.id
        }
        self.url = reverse('producto-list')
        
    def test_create_producto(self):
        response = self.client.post(self.url, self.producto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 1)
        self.assertEqual(Producto.objects.get().nombre, 'Test Producto')
        self.assertEqual(Producto.objects.get().creado_por, self.user)