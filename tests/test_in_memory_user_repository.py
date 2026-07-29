import pytest

from ai_architect.models.user import User
from ai_architect.repositories.in_memory_user_repository import InMemoryUserRepository


@pytest.fixture
def repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()


def test_starts_empty(repository):
    assert repository.list() == []
    assert repository.get(1) is None


def test_saved_user_can_be_read_back(repository):
    user = User(user_id=1, name="Alice", email="alice@example.com")

    repository.save(user)

    assert repository.get(1) == user
    assert repository.list() == [user]


def test_saving_same_id_overwrites(repository):
    repository.save(User(user_id=1, name="Alice", email="alice@example.com"))
    repository.save(User(user_id=1, name="Alice Smith", email="alice@example.com"))

    assert repository.get(1).name == "Alice Smith"
    assert len(repository.list()) == 1


def test_repository_stores_whatever_it_is_given(repository):
    """Storage applies no business rules - validation is the service's job."""
    repository.save(User(user_id=1, name="", email="not-an-email"))

    assert repository.get(1).email == "not-an-email"


def test_returned_list_is_a_copy(repository):
    repository.save(User(user_id=1, name="Alice", email="alice@example.com"))

    repository.list().clear()

    assert len(repository.list()) == 1
