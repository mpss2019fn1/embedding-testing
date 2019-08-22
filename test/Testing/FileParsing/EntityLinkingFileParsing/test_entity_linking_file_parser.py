import pytest

from src.Testing.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from test.Testing.base_test_case import BaseTestCase


class TestEntityLinkingFileParser(BaseTestCase):

    def test_entity_linking_file_parsing(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("embedding_label,knowledgebase_id\n" +
                  "Angela_Merkel,wd:Q567\n" +
                  "Hasso_Plattner,wd:Q71074", file=file_output)

        entity_linking = EntityLinkingFileParser.create_from_file(file)

        assert entity_linking["wd:Q567"] == "Angela_Merkel"
        assert entity_linking["wd:Q71074"] == "Hasso_Plattner"

        with pytest.raises(KeyError):
            # noinspection PyStatementEffect
            entity_linking["wd:Q1234"]

    def test_empty_line_is_ignored(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("embedding_label,knowledgebase_id\n" +
                  "Angela_Merkel,wd:Q567\n" +
                  "\n" +
                  "Hasso_Plattner,wd:Q71074", file=file_output)

        entity_linking = EntityLinkingFileParser.create_from_file(file)

        assert entity_linking["wd:Q567"] == "Angela_Merkel"
        assert entity_linking["wd:Q71074"] == "Hasso_Plattner"
