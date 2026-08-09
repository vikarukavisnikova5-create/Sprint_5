import random
import string
class GoodPassword:
    @staticmethod
    def generate_email():
        """Генерирует уникальный email."""
        number = random.randint(1000, 9999)
        return f"vika_{number}@yandex.ru"
    @staticmethod
    def generate_password(length=6):
        """Генерирует корректный пароль."""
        characters = string.ascii_letters + string.digits
        return "".join(
            random.choice(characters)
            for _ in range(length)
        )
class BadPassword:
    @staticmethod
    def generate_email():
        """Генерирует уникальный email."""
        number = random.randint(1000, 9999)
        return f"vika_{number}@yandex.ru"
    @staticmethod
    def generate_password(length=5):
        """Генерирует некорректный пароль."""
        characters = string.ascii_letters + string.digits
        return "".join(
            random.choice(characters)
            for _ in range(length)
        )
