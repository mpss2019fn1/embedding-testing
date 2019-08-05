import logging
from pathlib import Path

import yaml

from src.Testing.EntityLabel.entity_labels import EntityLabels
from src.Testing.FileParsing.abstract_file_parser import AbstractFileParser
from src.Testing.TaskConfiguration.task_category import TaskCategory


class TaskCategoryFileParser(AbstractFileParser):

    LABEL_ROOT = "configuration"
    LABEL_CATEGORIES = "categories"
    LABEL_CATEGORY = "category"
    LABEL_NAME = "name"
    LABEL_ENABLED = "enabled"
    LABEL_TASKS = "tasks"
    LABEL_TASK = "task"

    @staticmethod
    def create_categories_from_file(configuration_file, entity_labels):
        return TaskCategoryFileParser(configuration_file, entity_labels).create_categories()

    def __init__(self, configuration_file: Path, entity_labels: EntityLabels):
        super(TaskCategoryFileParser, self).__init__(configuration_file)
        self._entity_labels: EntityLabels = entity_labels

    def create_categories(self):
        with open(self._file_path, "r") as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[self.LABEL_ROOT][self.LABEL_CATEGORIES]
        categories = []

        if not configuration:
            return categories

        for category in configuration:
            category = category[self.LABEL_CATEGORY]
            categories.append(self._create_category_from_configuration(category))

        return categories

    def _create_category_from_configuration(self, configuration):
        name = self._extract_name(configuration)
        enabled = self._extract_enabled(configuration)
        tasks = self._extract_tasks(configuration)
        categories = self._extract_categories(configuration)
        return TaskCategory(name, enabled, tasks, categories)

    def _extract_enabled(self, configuration):
        enabled = str(configuration[self.LABEL_ENABLED]).lower()

        if enabled not in ["true", "false"]:
            logging.error("The provided boolean value for enabled are not valid")
            raise KeyError

        return enabled == "true"

    def _extract_name(self, configuration):
        if self.LABEL_NAME not in configuration:
            logging.error(f"Missing key {self.LABEL_NAME} in configuration")
            raise KeyError

        name = configuration[self.LABEL_NAME]

        if not name:
            logging.error("The provided task name must not be empty")
            raise KeyError

        return self._entity_labels[name]

    def _extract_tasks(self, configuration):
        from src.Testing.FileParsing.ConfigurationFileParsing.task_file_parser import TaskFileParser
        tasks = []
        task_configurations = configuration[self.LABEL_TASKS]
        if not task_configurations:
            return tasks

        task_file_parser = TaskFileParser(self._file_path)

        for task in task_configurations:
            task = task[self.LABEL_TASK]
            tasks.append(task_file_parser.create_task_from_configuration(task))
        return tasks

    def _extract_categories(self, configuration):
        categories = []
        category_configurations = configuration[TaskCategoryFileParser.LABEL_CATEGORIES]
        if not category_configurations:
            return categories

        for sub_category_configuration in category_configurations:
            sub_category_configuration = sub_category_configuration[TaskCategoryFileParser.LABEL_CATEGORY]
            categories.append(self._create_category_from_configuration(sub_category_configuration))
        return categories
