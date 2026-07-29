from __future__ import annotations

from typing import Protocol

from ai_architect.models.user import User


class UserRepository(Protocol):
    """Storage contract for users.

    Anything that provides these three methods *is* a UserRepository —
    no inheritance required.
    """

    def save(self, user: User) -> None:
        """Store the user, overwriting any existing user with the same id."""
        ...

    def get(self, user_id: int) -> User | None:
        """Return the user with this id, or None if there is no such user."""
        ...

    def list(self) -> list[User]:
        """Return every stored user."""
        ...
