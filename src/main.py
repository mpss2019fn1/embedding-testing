import argparse
import pickle
from pathlib import Path

from src.Evaluation.result_server import ResultServer
from src.Testing.FileParsing.ConfigurationFileParsing.task_category_file_parser import TaskCategoryFileParser
from src.Testing.FileParsing.ConfigurationFileParsing.task_configuration_file_parser import TaskConfigurationFileParser
from src.Testing.FileParsing.EmbeddingFileParsing.embedding_file_parser import EmbeddingFileParser
from src.Testing.FileParsing.EntityLabelFileParsing.entity_label_file_parser import EntityLabelFileParser
from src.Testing.FileParsing.EntityLinkingFileParsing.entity_linking_file_parser import EntityLinkingFileParser
from src.Testing.TestConfiguration.test_configuration import TestConfiguration
from src.Testing.TestExecution.test_executor import TestExecutor


def main(args):
    if "action" not in args or not args.action:
        print(f"No valid action provided.")
        exit(1)

    if args.action == "run":
        _run_tests(args)

    if args.action == "display":
        _display_results(args)


def _run_tests(args):
    entity_labels = EntityLabelFileParser.create_from_file(args.entity_labels)
    categories = TaskCategoryFileParser.create_categories_from_file(args.test_set_config, entity_labels)
    task_configurations = TaskConfigurationFileParser.create_configurations_from_file(args.test_set_config)
    entity_linkings = EntityLinkingFileParser.create_from_file(args.entity_mapping)
    embeddings = EmbeddingFileParser.create_from_file(args.embeddings)

    test_configuration = TestConfiguration(embeddings, entity_linkings, entity_labels, categories, task_configurations)

    test_executor = TestExecutor(test_configuration)
    test_category_results = list(test_executor.run())

    args.test_results.mkdirs()
    with args.test_results.open("w+") as output_stream:
        pickle.dump(test_category_results, output_stream)


def _display_results(args):
    result_server = ResultServer(args.test_results)
    result_server.run(debug=False)


def _initialize_parser():
    argument_parser = argparse.ArgumentParser()
    subparsers = argument_parser.add_subparsers()

    _initialize_run_parser(subparsers)
    _initialize_display_parser(subparsers)

    return argument_parser


def _initialize_run_parser(subparsers):
    run_parser = subparsers.add_parser("run")
    run_parser.set_defaults(action="run")

    run_parser.add_argument(
        "--test-set-config",
        type=Path,
        help="Path to the test set configuration file.",
        required=True
    )
    run_parser.add_argument(
        "--entity-mapping",
        type=Path,
        help="Path to the csv file containing knowledgebase to embedding tags entity mappings.",
        required=True
    )
    run_parser.add_argument(
        "--embeddings",
        type=Path,
        help=f"Path to the embeddings file (word2vec format)",
        required=True
    )
    run_parser.add_argument(
        "--entity-labels",
        type=Path,
        help=f"Path to the file containing entity-labels",
        required=False
    )
    run_parser.add_argument(
        "--test-results",
        type=Path,
        help=f"The path where to store the test execution results",
        required=True
    )


def _initialize_display_parser(subparsers):
    display_parser = subparsers.add_parser("display")
    display_parser.set_defaults(action="display")

    display_parser.add_argument(
        "--test-results",
        type=Path,
        help=f"Path to the stored test results",
        required=True
    )


if __name__ == "__main__":
    parser = _initialize_parser()
    main(parser.parse_args())
