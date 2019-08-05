import pytest

from src.Testing.FileParsing.EntityLabelFileParsing.entity_label_file_parser import EntityLabelFileParser
from test.Testing.base_test_case import BaseTestCase


class TestEntityLabelFileParsing(BaseTestCase):

    def test_entity_linking_file_parsing(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("knowledgebase_id,label\n" +
                  "wd:Q567,Angela Merkel\n" +
                  "wd:Q71074,Hasso Plattner", file=file_output)

        entity_label = EntityLabelFileParser.create_from_file(file)

        assert entity_label["wd:Q567"] == "Angela Merkel"
        assert entity_label["wd:Q71074"] == "Hasso Plattner"

        assert entity_label["wd:Q1234"] == "wd:Q1234"

    def test_empty_line_is_ignored(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("embedding_label,knowledgebase_id\n" +
                  "wd:Q567,Angela Merkel\n" +
                  "\n" +
                  "wd:Q71074,Hasso Plattner", file=file_output)

        entity_label = EntityLabelFileParser.create_from_file(file)

        assert entity_label["wd:Q567"] == "Angela Merkel"
        assert entity_label["wd:Q71074"] == "Hasso Plattner"
