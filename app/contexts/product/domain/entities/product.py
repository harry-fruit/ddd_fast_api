from uuid import uuid4
from app.contexts.products.domain.value_objects.price import Price

class Product:
    def __init__(self, name: str, price: Price, stock: int, id: str = None):
        self.id = id or str(uuid4())
        self.name = self._validate_name(name)
        self.price = price
        self.stock = stock

    def _validate_name(self, name: str) -> str:
        if len(name) < 3:
            raise ValueError("O nome do produto deve ter pelo menos 3 caracteres.")
        return name

    def update_stock(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.stock = quantity