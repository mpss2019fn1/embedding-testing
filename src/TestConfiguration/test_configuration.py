from typing import List

from src.Embeddings.embeddings import Embeddings
from src.EntityLinking.entity_linkings import EntityLinkings
from src.Task import TaskType
from src.TaskConfiguration import TaskCategory, TaskConfiguration


class TestConfiguration:

    def __init__(self, embeddings: Embeddings, entity_linkings: EntityLinkings, categories: List[TaskCategory],
                 task_configurations: List[TaskConfiguration]):
        self.embeddings = embeddings
        self.entity_linkings = entity_linkings
        self.categories = categories
        self.task_configurations = task_configurations

    def is_enabled(self, task_type: TaskType):
        return any(config for config in self.task_configurations if config.task_type == task_type and config.enabled)
