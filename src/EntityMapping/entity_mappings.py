import time


class EntityMappings:

    def __init__(self):
        self.imported = time.time()
        self._entity_mappings = {}

    def add(self, knowledgebase_id, embedding_tag):
        self._entity_mappings[knowledgebase_id] = embedding_tag

    def __getitem__(self, item):
        return self._entity_mappings[item]

    def __contains__(self, item):
        return item in self._entity_mappings
