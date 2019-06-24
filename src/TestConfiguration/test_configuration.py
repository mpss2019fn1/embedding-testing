from typing import List

from src.Embedding.embedding import Embedding
from src.EntityLinking.entity_linkings import EntityLinkings
from src.Task import TaskType
from src.TaskConfiguration import TaskCategory, TaskConfiguration


class TestConfiguration:

    def __init__(self, embedding: Embedding, entity_linkings: EntityLinkings, categories: List[TaskCategory],
                 task_configurations: List[TaskConfiguration]):
        self.embedding = embedding
        self.entity_linkings = entity_linkings
        self.categories = categories
        self.task_configurations = task_configurations

    def is_enabled(self, task_type: TaskType):
        return any(config for config in self.task_configurations if config.task_type == task_type and config.enabled)
