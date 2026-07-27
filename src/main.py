from src.services.user_service import InvalidEmailError, UserService


def main():
    service = UserService()

    service.create_user(1, "Alice", "alice@example.com")
    service.create_user(2, "Bob", "bob@example.com")

    try:
        service.create_user(3, "Charlie", "charlie-no-email")
    except InvalidEmailError as e:
        print(f"Failed to create user: {e}")

    for name in service.get_all_user_names():
        print(name)


if __name__ == "__main__":
    main()
