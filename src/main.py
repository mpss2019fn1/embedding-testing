import argparse
from pathlib import Path

from src.Evaluation.result_server import result_server
from src.Testing.FileParsing.ConfigurationFileParsing.task_category_file_parser import TaskCategoryFileParser
from src.Testing.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.Testing.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.Testing.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.Testing.TestConfiguration.test_configuration import TestConfiguration
from src.Testing.TestExecution.test_executor import TestExecutor


def main(args):
    categories = TaskCategoryFileParser.create_categories_from_file(args.test_set_config)
    task_configurations = TaskConfigurationFileParser.create_configurations_from_file(args.test_set_config)
    entity_linkings = EntityLinkingFileParser.create_from_file(args.entity_mapping)
    embeddings = EmbeddingFileParser.create_from_file(args.embeddings)

    test_configuration = TestConfiguration(embeddings, entity_linkings, categories, task_configurations)

    test_executor = TestExecutor(test_configuration)
    test_category_results = list(test_executor.run())

    result_server.config["results"] = test_category_results
    result_server.run(debug=False)


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
