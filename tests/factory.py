import factory
from product.models import Category, Brand, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = "Mobile"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    name = "Apple"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = "I Phone"
    description = "Nice Product"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
