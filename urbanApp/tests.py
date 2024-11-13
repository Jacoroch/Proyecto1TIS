# urbanApp/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        # Crear un producto de ejemplo para las pruebas
        self.product = Product.objects.create(
            name="Producto de Prueba",
            price=100.00,
            description="Descripción del producto de prueba"
        )
        
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser1', password='Password1.')

    def test_product_creation(self):
        # Prueba para verificar si el producto se creó correctamente
        product = Product.objects.get(name="Producto de Prueba")
        self.assertEqual(product.price, 100.00)
        self.assertEqual(product.description, "Descripción del producto de prueba")

    def test_product_detail_view(self):
        # Autentica al usuario de prueba usando force_login
        self.client.force_login(self.user)
        
        # Probar la vista de detalles del producto
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

