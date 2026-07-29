from __future__ import annotations

import re

from ai_architect.models.user import User
from ai_architect.repositories.user_repository import UserRepository

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class InvalidEmailError(Exception):
    pass


class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def create_user(self, user: User) -> User:
        email = user.email.strip().lower()
        if not EMAIL_PATTERN.match(email):
            raise InvalidEmailError(f"Invalid email: {user.email}")
        user.email = email
        self._repository.save(user)
        return user

    def get_user(self, user_id: int) -> User | None:
        return self._repository.get(user_id)

    def get_all_user_names(self) -> list[str]:
        return [user.name for user in self._repository.list()]
