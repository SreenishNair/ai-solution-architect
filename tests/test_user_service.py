import pytest

from ai_architect.models.user import User
from ai_architect.services.user_service import (
    InvalidEmailError,
    UserService,
)


def test_create_valid_user():
    service = UserService()

    user = User(
        user_id=1,
        name="Alice",
        email="alice@example.com",
    )

    created = service.create_user(user)

    assert created.user_id == 1
    assert created.name == "Alice"
    assert created.email == "alice@example.com"


def test_reject_invalid_email():
    service = UserService()

    user = User(
        user_id=1,
        name="Alice",
        email="invalid-email",
    )

    with pytest.raises(InvalidEmailError):
        service.create_user(user)


def test_retrieve_existing_user():
    service = UserService()

    user = User(
        user_id=1,
        name="Alice",
        email="alice@example.com",
    )
    service.create_user(user)

    retrieved = service.get_user(1)

    assert retrieved == user


def test_retrieve_missing_user():
    service = UserService()

    retrieved = service.get_user(999)

    assert retrieved is None
