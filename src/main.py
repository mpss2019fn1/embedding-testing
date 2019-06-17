import argparse
from pathlib import Path

from src.TaskConfiguration import TaskCategoryCollectionFactory


def main(args):
    test_configuration = TaskCategoryCollectionFactory.create_categories_from_file(args.test_set_config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test-set-config",
        type=Path,
        help="Path to the test set configuration file.",
        required=True
    )
    main(parser.parse_args())
