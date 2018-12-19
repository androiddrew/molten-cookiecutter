from molten.errors import MoltenError


class EntityNotFound(MoltenError):
    """Raised when an entity is not found using an `exists` check in sqlalchemy."""
