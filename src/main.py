import argparse
from pathlib import Path

from src.Embedding.embedding_factory import EmbeddingFactory
from src.EntityLinking.entity_linkings_factory import EntityLinkingsFactory
from src.TaskConfiguration import TaskConfigurationFactory, TaskCategoryFactory
from src.TestConfiguration.test_configuration import TestConfiguration


def main(args):
    categories = TaskCategoryFactory.create_categories_from_file(args.test_set_config)
    task_configurations = TaskConfigurationFactory.create_configurations_from_file(args.test_set_config)
    entity_linkings = EntityLinkingsFactory.create_from_file(args.entity_mapping)
    embeddings = EmbeddingFactory.create_from_file(args.embeddings)

    test_configuration = TestConfiguration(embeddings, entity_linkings, categories, task_configurations)


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
    parser.add_argument(
        "--embeddings",
        type=Path,
        help=f"Path to the embeddings file (word2vec format)",
        required=True
    )
    main(parser.parse_args())
