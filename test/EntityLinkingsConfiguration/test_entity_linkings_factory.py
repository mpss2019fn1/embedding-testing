from src.EntityLinkingsConfiguration.entity_linkings_factory import EntityLinkingsFactory
from test.base_test_case import BaseTestCase


class TestEntityLinkingsFactory(BaseTestCase):

    def test_create_entity_linkings_from_file(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"embedding_label,knowledgebase_id\n" +
                  "Angela_Merkel,wd:Q567\n" +
                  "Donald_Trump,wd:Q22686", file=file_output)

        entity_linkings = EntityLinkingsFactory.create_from_file(file)

        self.assertEqual(2, len(entity_linkings))
        self.assertEqual(entity_linkings["wd:Q567"], "Angela_Merkel")
        self.assertEqual(entity_linkings["wd:Q22686"], "Donald_Trump")
