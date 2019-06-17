import argparse
from pathlib import Path

from src.EntityMappingConfiguration.entity_linkings_factory import EntityMappingsFactory
from src.TaskConfiguration import TaskCategoryCollectionFactory


def main(args):
    test_configuration = TaskCategoryCollectionFactory.create_categories_from_file(args.test_set_config)
    entity_mappings = EntityMappingsFactory.create_from_configuration_file(args.entity_mapping)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test-set-config",
        type=Path,
        help="Path to the test set configuration file.",
        required=True
    )
    parser.add_argument(
        "--entity-mapping",
        type=Path,
        help="Path to the csv file containing knowledgebase to embedding tags entity mappings.",
        required=True
    )
    main(parser.parse_args())
