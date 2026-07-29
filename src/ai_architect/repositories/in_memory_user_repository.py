from __future__ import annotations

from ai_architect.models.user import User


class InMemoryUserRepository:
    """Dict-backed UserRepository. Data lives only as long as the process."""

    def __init__(self) -> None:
        self._users: dict[int, User] = {}

    def save(self, user: User) -> None:
        self._users[user.user_id] = user

    def get(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def list(self) -> list[User]:
        return list(self._users.values())
