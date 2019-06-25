from src.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from test.base_test_case import BaseTestCase


class TestEntityLinkingsFactory(BaseTestCase):

    def test_create_entity_linkings_from_file(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"embedding_label,knowledgebase_id\n" +
                  "Angela_Merkel,wd:Q567\n" +
                  "Donald_Trump,wd:Q22686", file=file_output)

        entity_linkings = EntityLinkingFileParser.create_from_file(file)

        assert 2 == len(entity_linkings)
        assert entity_linkings["wd:Q567"] == "Angela_Merkel"
        assert entity_linkings["wd:Q22686"] == "Donald_Trump"
