import csv

from src.EntityLinking.entity_linkings import EntityLinkings


class EntityLinkingsFactory:
    COLUMN_INDEX_KNOWLEDGEBASE_ID = 1
    COLUMN_INDEX_EMBEDDING_LABEL = 0

    @staticmethod
    def create_from_configuration_file(configuration_file):
        with open(configuration_file, 'r') as csv_stream:
            csv_reader = csv.reader(csv_stream, delimiter=',')
            entity_mappings = EntityLinkings()

            next(csv_reader, None)  # skip header
            for row in csv_reader:
                if not row:
                    continue

                knowledgebase_id = row[EntityLinkingsFactory.COLUMN_INDEX_KNOWLEDGEBASE_ID]
                embedding_tag = row[EntityLinkingsFactory.COLUMN_INDEX_EMBEDDING_LABEL]
                entity_mappings.add(knowledgebase_id, embedding_tag)

            return entity_mappings
