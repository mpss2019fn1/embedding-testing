from typing import List

from src.Embedding.embedding import Embedding
from src.EntityLinking.entity_linkings import EntityLinkings
from src.Task.task_type import TaskType
from src.TaskConfiguration.task_category import TaskCategory
from src.TaskConfiguration.task_configuration import TaskConfiguration


class TestConfiguration:

    def __init__(self, embedding: Embedding, entity_linking: EntityLinkings, categories: List[TaskCategory],
                 task_configurations: List[TaskConfiguration]):
        self.embedding = embedding
        self.entity_linking = entity_linking
        self.categories = categories
        self.task_configurations = task_configurations

    def is_enabled(self, task_type: TaskType):
        return any(config for config in self.task_configurations if config.task_type == task_type and config.enabled)
