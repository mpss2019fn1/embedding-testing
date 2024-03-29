from typing import List

from src.Testing.Embedding.embedding import Embedding
from src.Testing.EntityLabel.entity_labels import EntityLabels
from src.Testing.EntityLinking.entity_linkings import EntityLinkings
from src.Testing.Task.task_type import TaskType
from src.Testing.TaskConfiguration.task_category import TaskCategory
from src.Testing.TaskConfiguration.task_configuration import TaskConfiguration


class TestConfiguration:

    def __init__(self, embedding: Embedding, entity_linking: EntityLinkings, entity_labels: EntityLabels,
                 categories: List[TaskCategory], task_configurations: List[TaskConfiguration]):
        self.embedding = embedding
        self.entity_labels = entity_labels
        self.entity_linking = entity_linking
        self.categories = categories
        self.task_configurations = task_configurations

    def is_enabled(self, task_type: TaskType):
        return any(config for config in self.task_configurations if config.task_type == task_type and config.enabled)
