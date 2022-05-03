from typing import Optional


class Account:
    name: str
    email: str
    password: str
    phone: str

    def __init__(self, name: str, email: Optional[str] = None, password: Optional[str] = None, phone: Optional[str] = None) -> None:
        self.name = name
        self.email = email
        self.password = str(hash(password)) if password else None
        self.phone = phone
