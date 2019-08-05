import csv
from pathlib import Path

from src.Testing.EntityLabel.entity_labels import EntityLabels
from src.Testing.FileParsing.abstract_file_parser import AbstractFileParser


class EntityLabelFileParser(AbstractFileParser):
    COLUMN_INDEX_KNOWLEDGEBASE_ID = 0
    COLUMN_INDEX_EMBEDDING_LABEL = 1

    @staticmethod
    def create_from_file(configuration_file: Path):
        if not configuration_file.exists():
            return EntityLabels()

        with configuration_file.open("r") as csv_stream:
            csv_reader = csv.reader(csv_stream, delimiter=',')
            entity_labels = EntityLabels()

            next(csv_reader, None)  # skip header
            for row in csv_reader:
                if not row:
                    continue

                knowledgebase_id = row[EntityLabelFileParser.COLUMN_INDEX_KNOWLEDGEBASE_ID]
                entity_label = row[EntityLabelFileParser.COLUMN_INDEX_EMBEDDING_LABEL]
                entity_labels.add(knowledgebase_id, entity_label)

            return entity_labels
