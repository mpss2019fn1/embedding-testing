import time

from src.Testing.EntityLinking.entity_linkings import EntityLinkings


class TestEntityLinking:

    def test_initialization(self):
        entity_mapping = EntityLinkings()

        assert entity_mapping is not None

    def test_add(self):
        entity_mapping = EntityLinkings()
        entity_mapping.add("wd:Q567", "Angela_Merkel")

        assert "wd:Q567" in entity_mapping
        assert len(entity_mapping) == 1

    def test_fetching_mapping(self):
        entity_mapping = EntityLinkings()
        entity_mapping.add("wd:Q567", "Angela_Merkel")

        assert entity_mapping["wd:Q567"] == "Angela_Merkel"
