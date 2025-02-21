from app.contexts.product.domain.entities.product import Product
from app.contexts.product.domain.value_objects.price import Price
from app.contexts.product.infrastructure.repositories.product_repository import ProductRepository

class AddProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name: str, price: float, stock: int):
        price_vo = Price(price)
        product = Product(name=name, price=price_vo, stock=stock)
        return self.repository.save(product)