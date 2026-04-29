from enum import Enum

class UserRole(str, Enum):
    """
    Перечисленние ролей
    """
    ADMIN = 'ADMIN'
    USER = 'USER'
    GUEST = 'GUEST'
    MODERATOR = 'MODERATOR'