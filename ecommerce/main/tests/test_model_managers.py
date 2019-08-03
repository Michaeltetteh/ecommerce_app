from decimal import Decimal
from django.test import TestCase
from main import models


class TestModel(TestCase):
    def test_active_model_manager_works(self):
        models.Product.objects.create(
            name="Django For API",
            price=Decimal("23.00"))

        models.Product.objects.create(
            name="Django RestFramework",
            price=Decimal("33.00"))

        models.Product.objects.create(
            name="React Web app",
            price=Decimal("22.00"),
            active=False)
        self.assertEqual(len(models.Product.objects.active()), 2)
