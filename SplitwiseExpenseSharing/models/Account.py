class Account:
    id: str
    name: str
    email: str
    mobile: str

    def __init__(self, userId: str, name: str, email: str, mobile: str) -> None:
        self.id = userId
        self.name = name
        self.email = email
        self.mobile = mobile
