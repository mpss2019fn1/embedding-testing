from typing import List

from src.Embeddings.embeddings import Embeddings
from src.EntityLinking.entity_linkings import EntityLinkings
from src.TaskConfiguration import TaskCategory, TaskConfiguration


class TestConfiguration:

    def __init__(self, embeddings: Embeddings, entity_linkings: EntityLinkings, categories: List[TaskCategory],
                 task_configurations: List[TaskConfiguration]):
        self.embeddings = embeddings
        self.entity_linkings = entity_linkings
        self.categories = categories
        self.task_configurations = task_configurations
