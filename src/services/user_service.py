from src.models.user import User


class InvalidEmailError(Exception):
    pass


class UserService:
    def __init__(self):
        self._users: dict[int, User] = {}

    def create_user(self, id: int, name: str, email: str) -> User:
        if "@" not in email:
            raise InvalidEmailError(f"Invalid email: {email}")
        user = User(id=id, name=name, email=email)
        self._users[id] = user
        return user

    def get_user(self, id: int) -> User | None:
        return self._users.get(id)

    def get_all_user_names(self) -> list[str]:
        
        return [user.name for user in self._users.values()]
