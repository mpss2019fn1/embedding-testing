import logging

import yaml

from src.FileParsing.abstract_file_parser import AbstractFileParser
from src.TaskConfiguration import TaskCategory


class CategoryFileParser(AbstractFileParser):

    LABEL_ROOT = "configuration"
    LABEL_CATEGORIES = "categories"
    LABEL_CATEGORY = "category"
    LABEL_NAME = "name"
    LABEL_ENABLED = "enabled"
    LABEL_TASKS = "tasks"
    LABEL_TASK = "task"

    @staticmethod
    def create_categories_from_file(configuration_file):
        with open(configuration_file, 'r') as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[CategoryFileParser.LABEL_ROOT][
            CategoryFileParser.LABEL_CATEGORIES]
        categories = []
        for category in configuration:
            category = category[CategoryFileParser.LABEL_CATEGORY]
            categories.append(CategoryFileParser.create_category_from_configuration(category))

        return categories

    @staticmethod
    def create_category_from_configuration(configuration):
        name = CategoryFileParser._extract_name(configuration)
        enabled = CategoryFileParser._extract_enabled(configuration)
        tasks = CategoryFileParser._extract_tasks(configuration)
        categories = CategoryFileParser._extract_categories(configuration)
        return TaskCategory(name, enabled, tasks, categories)

    @staticmethod
    def _extract_enabled(configuration):
        enabled = str(configuration[CategoryFileParser.LABEL_ENABLED]).lower()

        if enabled not in ["true", "false"]:
            logging.error("The provided boolean value for enabled are not valid")
            raise KeyError

        return enabled == "true"

    @staticmethod
    def _extract_name(configuration):
        if CategoryFileParser.LABEL_NAME not in configuration:
            logging.error(f"Missing key {CategoryFileParser.LABEL_NAME} in configuration")
            raise KeyError

        name = configuration[CategoryFileParser.LABEL_NAME]

        if not name:
            logging.error("The provided task name must not be empty")
            raise KeyError

        return name

    @staticmethod
    def _extract_tasks(configuration):
        from src.Task import TaskFileParser

        tasks = []
        task_configurations = configuration[CategoryFileParser.LABEL_TASKS]
        if not task_configurations:
            return tasks

        for task in task_configurations:
            task = task[CategoryFileParser.LABEL_TASK]
            tasks.append(TaskFileParser.create_task_from_configuration(task))
        return tasks

    @staticmethod
    def _extract_categories(configuration):
        categories = []
        category_configurations = configuration[CategoryFileParser.LABEL_CATEGORIES]
        if not category_configurations:
            return categories

        for sub_category_configuration in category_configurations:
            sub_category_configuration = sub_category_configuration[CategoryFileParser.LABEL_CATEGORY]
            categories.append(CategoryFileParser.create_category_from_configuration(sub_category_configuration))
        return categories
