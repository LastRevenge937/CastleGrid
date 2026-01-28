import time
import uuid

class Doctrine:
    """
    Versioned, immutable, auditable defensive doctrine
    """
    def __init__(self, name, author, content):
        self.id = str(uuid.uuid4())
        self.name = name
        self.author = author
        self.version = 1
        self.created = time.time()
        self.content = content
        self.approved = False

    def bump(self, new_content):
        """
        Create a new version of this doctrine
        """
        self.version += 1
        self.content = new_content
