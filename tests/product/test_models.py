import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name="Mobile")
        # Assert
        assert x.__str__() == "Mobile"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        x = brand_factory(name="Apple")
        # Assert
        assert x.__str__() == "Apple"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        x = product_factory(name="I Phone")
        # Assert
        assert x.__str__() == "I Phone"
