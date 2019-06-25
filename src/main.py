import argparse
from pathlib import Path

from src.FileParsing.ConfigurationFileParsing.task_category_file_parser import TaskCategoryFileParser
from src.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.TestConfiguration.test_configuration import TestConfiguration


def main(args):
    categories = TaskCategoryFileParser.create_categories_from_file(args.test_set_config)
    task_configurations = TaskConfigurationFileParser.create_configurations_from_file(args.test_set_config)
    entity_linkings = EntityLinkingFileParser.create_from_file(args.entity_mapping)
    embeddings = EmbeddingFileParser.create_from_file(args.embeddings)

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
