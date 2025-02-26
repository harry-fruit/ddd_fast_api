class Price:
    def __init__(self, value: float):
        if value < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.value = value