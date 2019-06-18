import time

from src.EntityLinking.entity_linkings import EntityLinkings


class TestEntityMapping:

    def test_initialization(self):
        entity_mapping = EntityLinkings()

        assert entity_mapping is not None
        assert entity_mapping.imported < time.time()

    def test_add(self):
        entity_mapping = EntityLinkings()
        entity_mapping.add("wd:Q567", "Angela_Merkel")

        assert "wd:Q567" in entity_mapping
        assert 1 == len(entity_mapping)

    def test_fetching_mapping(self):
        entity_mapping = EntityLinkings()
        entity_mapping.add("wd:Q567", "Angela_Merkel")

        assert entity_mapping["wd:Q567"] == "Angela_Merkel"
