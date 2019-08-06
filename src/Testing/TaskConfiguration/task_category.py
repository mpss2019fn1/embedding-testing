import uuid
from typing import List


class TaskCategory:

    def __init__(self, name, enabled, tasks, categories):
        self.name = name
        self.enabled = enabled
        self.tasks = tasks
        self.categories = categories
        self.id = uuid.uuid4()

    def categories_recursive(self) -> List["TaskCategory"]:
        categories: List["TaskCategory"] = self.categories

        for category in self.categories:
            categories.extend(category.categories_recursive())

        return categories
