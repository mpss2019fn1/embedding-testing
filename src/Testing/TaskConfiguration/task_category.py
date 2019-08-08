import uuid
from pathlib import Path


class TaskCategory:

    def __init__(self, name, enabled, tasks, categories, embedding_filter: Path):
        self.name = name
        self.enabled = enabled
        self.tasks = tasks
        self.categories = categories
        self.embedding_filter: Path = embedding_filter
        self.id = uuid.uuid4()
