import re

from ai_architect.models.user import User

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class InvalidEmailError(Exception):
    pass


class UserService:
    def __init__(self):
        self._users: dict[int, User] = {}

    def create_user(self, user: User) -> User:
        email = user.email.strip().lower()
        if not EMAIL_PATTERN.match(email):
            raise InvalidEmailError(f"Invalid email: {user.email}")
        user.email = email
        self._users[user.user_id] = user
        return user

    def get_user(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def get_all_user_names(self) -> list[str]:
        
        return [user.name for user in self._users.values()]
