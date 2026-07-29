import pytest

from ai_architect.models.user import User
from ai_architect.repositories.in_memory_user_repository import InMemoryUserRepository
from ai_architect.services.user_service import InvalidEmailError, UserService


@pytest.fixture
def service() -> UserService:
    return UserService(InMemoryUserRepository())


def test_created_user_can_be_retrieved(service):
    service.create_user(User(user_id=1, name="Alice", email="alice@example.com"))

    retrieved = service.get_user(1)

    assert retrieved is not None
    assert retrieved.name == "Alice"
    assert retrieved.email == "alice@example.com"


def test_unknown_user_is_not_found(service):
    assert service.get_user(999) is None


def test_email_is_normalised_before_storing(service):
    service.create_user(User(user_id=1, name="Alice", email="  ALICE@Example.COM  "))

    assert service.get_user(1).email == "alice@example.com"


def test_invalid_email_is_rejected(service):
    with pytest.raises(InvalidEmailError):
        service.create_user(User(user_id=1, name="Alice", email="invalid-email"))


def test_rejected_user_is_not_stored(service):
    with pytest.raises(InvalidEmailError):
        service.create_user(User(user_id=1, name="Alice", email="invalid-email"))

    assert service.get_user(1) is None
    assert service.get_all_user_names() == []


def test_no_names_before_any_user_is_created(service):
    assert service.get_all_user_names() == []


def test_all_created_users_are_listed(service):
    service.create_user(User(user_id=1, name="Alice", email="alice@example.com"))
    service.create_user(User(user_id=2, name="Bob", email="bob@example.com"))

    assert service.get_all_user_names() == ["Alice", "Bob"]


def test_saving_same_id_replaces_the_user(service):
    service.create_user(User(user_id=1, name="Alice", email="alice@example.com"))
    service.create_user(User(user_id=1, name="Alice Smith", email="alice@example.com"))

    assert service.get_all_user_names() == ["Alice Smith"]


class RecordingRepository:
    """A stand-in repository that records what the service asked it to do."""

    def __init__(self):
        self.saved: list[User] = []

    def save(self, user):
        self.saved.append(user)

    def get(self, user_id):
        return None

    def list(self):
        return []


def test_service_saves_through_whatever_repository_it_is_given():
    repository = RecordingRepository()
    service = UserService(repository)

    service.create_user(User(user_id=1, name="Alice", email="alice@example.com"))

    assert len(repository.saved) == 1
    assert repository.saved[0].name == "Alice"


def test_service_does_not_save_invalid_users():
    repository = RecordingRepository()
    service = UserService(repository)

    with pytest.raises(InvalidEmailError):
        service.create_user(User(user_id=1, name="Alice", email="invalid-email"))

    assert repository.saved == []
