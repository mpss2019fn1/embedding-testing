import uuid


class TaskCategory:

    def __init__(self, name, enabled, tasks, categories):
        self.name = name
        self.enabled = enabled
        self.tasks = tasks
        self.categories = categories
        self.id = uuid.uuid4()
