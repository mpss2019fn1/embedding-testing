import csv

from src.EntityMapping.entity_mappings import EntityMappings


class EntityMappingsFactory:
    COLUMN_INDEX_KNOWLEDGEBASE_ID = 1
    COLUMN_INDEX_EMBEDDING_LABEL = 0

    @staticmethod
    def create_from_configuration_file(configuration_file):
        with open(configuration_file, 'r') as csv_stream:
            csv_reader = csv.reader(csv_stream, delimiter=',')
            entity_mappings = EntityMappings()

            next(csv_reader, None)  # skip header
            for row in csv_reader:
                knowledgebase_id = row[EntityMappingsFactory.COLUMN_INDEX_KNOWLEDGEBASE_ID]
                embedding_tag = row[EntityMappingsFactory.COLUMN_INDEX_EMBEDDING_LABEL]
                entity_mappings.add(embedding_tag, knowledgebase_id)

            return entity_mappings
