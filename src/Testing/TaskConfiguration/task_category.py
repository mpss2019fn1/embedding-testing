import uuid
from pathlib import Path


class TaskCategory:

    def __init__(self, name, enabled, tasks, categories, considered_entities_file: Path):
        self.name = name
        self.enabled = enabled
        self.tasks = tasks
        self.categories = categories
        self.considered_entities_file: Path = considered_entities_file
        self.id = uuid.uuid4()
