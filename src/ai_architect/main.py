from ai_architect.models.user import User
from ai_architect.services.user_service import InvalidEmailError, UserService


def main():
    service = UserService()

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
