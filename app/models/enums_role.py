from enum import Enum

class UserRole(str, Enum):
    """
    Перечисленние ролей
    """
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'
    MODERATOR = 'moderator'