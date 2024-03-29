import csv

from src.Testing.EntityLinking.entity_linkings import EntityLinkings
from src.Testing.FileParsing.abstract_file_parser import AbstractFileParser


class EntityLinkingFileParser(AbstractFileParser):
    COLUMN_INDEX_KNOWLEDGEBASE_ID = 1
    COLUMN_INDEX_EMBEDDING_LABEL = 0

    @staticmethod
    def create_from_file(configuration_file):
        with open(configuration_file, 'r') as csv_stream:
            csv_reader = csv.reader(csv_stream, delimiter=',')
            entity_mappings = EntityLinkings()

            next(csv_reader, None)  # skip header
            for row in csv_reader:
                if not row:
                    continue

                knowledgebase_id = row[EntityLinkingFileParser.COLUMN_INDEX_KNOWLEDGEBASE_ID]
                embedding_tag = row[EntityLinkingFileParser.COLUMN_INDEX_EMBEDDING_LABEL]
                entity_mappings.add(knowledgebase_id, embedding_tag)

            return entity_mappings
