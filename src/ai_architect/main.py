from ai_architect.models.user import User
from ai_architect.repositories.in_memory_user_repository import InMemoryUserRepository
from ai_architect.services.user_service import InvalidEmailError, UserService


def main():
    repository = InMemoryUserRepository()
    service = UserService(repository)

    service.create_user(User(user_id=1, name="Alice", email="alice@example.com"))
    service.create_user(User(user_id=2, name="Bob", email="bob@example.com"))

    try:
        service.create_user(User(user_id=3, name="Charlie", email="charlie-no-email"))
    except InvalidEmailError as e:
        print(f"Failed to create user: {e}")

    for name in service.get_all_user_names():
        print(name)


if __name__ == "__main__":
    main()
