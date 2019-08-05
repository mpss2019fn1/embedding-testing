class EntityLabels:

    def __init__(self):
        self._entity_labels = {}

    def add(self, knowledgebase_id, entity_label):
        self._entity_labels[knowledgebase_id] = entity_label

    def __getitem__(self, knowledgebase_id):
        if knowledgebase_id in self._entity_labels:
            return self._entity_labels[knowledgebase_id]
        return knowledgebase_id

    def __contains__(self, knowledgebase_id):
        return knowledgebase_id in self._entity_labels

    def __len__(self):
        return len(self._entity_labels)
