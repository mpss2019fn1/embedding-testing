import time
import unittest

from src.EntityLinking.entity_linkings import EntityLinkings


class TestEntityMapping(unittest.TestCase):

    def test_initialization(self):
        entity_mapping = EntityLinkings()

        self.assertIsNotNone(entity_mapping)
        self.assertLess(entity_mapping.imported, time.time())

    def test_add(self):
        entity_mapping = EntityLinkings()
        entity_mapping.add("wd:Q567", "Angela_Merkel")

        self.assertTrue("Q567" in entity_mapping)
        self.assertEqual(1, len(entity_mapping))

    def test_fetching_mapping(self):
        entity_mapping = EntityLinkings()
        entity_mapping.add("wd:Q567", "Angela_Merkel")

        self.assertEqual(entity_mapping["Q567"], "Angela_Merkel")
