from uuid import uuid4
from app.contexts.user.domain.value_objects.email import Email

class User:
    def __init__(self, name: str, email: Email, password: str, id: str = None):
        self.id = id or str(uuid4())
        self.name = self._validate_name(name)
        self.email = email
        self.password = password  #TODO: Senha deve ser armazenada criptografada!

    def _validate_name(self, name: str) -> str:
        if len(name) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        return name