import time

from src.EntityMapping.entity_mappings import EntityMappings
from test.base_test_case import BaseTestCase


class TestEntityMapping(BaseTestCase):

    def test_initialization(self):
        entity_mapping = EntityMappings()

        self.assertIsNotNone(entity_mapping)
        self.assertLess(entity_mapping.imported, time.time())

    def test_add(self):
        entity_mapping = EntityMappings()
        entity_mapping.add("Angela_Merkel", "Q567")

        self.assertTrue("Q567" in entity_mapping)

    def test_fetching_mapping(self):
        entity_mapping = EntityMappings()
        entity_mapping.add("Angela_Merkel", "Q567")

        self.assertEqual(entity_mapping["Q567"], "Angela_Merkel")
