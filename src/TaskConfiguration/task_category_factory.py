import logging

from src.TaskConfiguration import TaskCategory


class TaskCategoryFactory:

    LABEL_NAME = "name"
    LABEL_ENABLED = "enabled"
    LABEL_TASKS = "tasks"
    LABEL_TASK = "task"
    LABEL_CATEGORIES = "categories"
    LABEL_CATEGORY = "category"

    @staticmethod
    def create_category_from_configuration(configuration):
        name = TaskCategoryFactory._extract_name(configuration)
        enabled = TaskCategoryFactory._extract_enabled(configuration)
        tasks = TaskCategoryFactory._extract_tasks(configuration)
        categories = TaskCategoryFactory._extract_categories(configuration)
        return TaskCategory(name, enabled, tasks, categories)

    @staticmethod
    def _extract_enabled(configuration):
        enabled = str(configuration[TaskCategoryFactory.LABEL_ENABLED]).lower()

        if enabled not in ["true", "false"]:
            logging.error("The provided boolean value for enabled are not valid")
            raise KeyError

        return enabled == "true"

    @staticmethod
    def _extract_name(configuration):
        if TaskCategoryFactory.LABEL_NAME not in configuration:
            logging.error(f"Missing key {TaskCategoryFactory.LABEL_NAME} in configuration")
            raise KeyError

        name = configuration[TaskCategoryFactory.LABEL_NAME]

        if not name:
            logging.error("The provided task name must not be empty")
            raise KeyError

        return name

    @staticmethod
    def _extract_tasks(configuration):
        from src.Task import TaskFactory

        tasks = []
        task_configurations = configuration[TaskCategoryFactory.LABEL_TASKS]
        if not task_configurations:
            return tasks

        for task in task_configurations:
            task = task[TaskCategoryFactory.LABEL_TASK]
            tasks.append(TaskFactory.create_task_from_configuration(task))
        return tasks

    @staticmethod
    def _extract_categories(configuration):
        categories = []
        category_configurations = configuration[TaskCategoryFactory.LABEL_CATEGORIES]
        if not category_configurations:
            return categories

        for sub_category_configuration in category_configurations:
            sub_category_configuration = sub_category_configuration[TaskCategoryFactory.LABEL_CATEGORY]
            categories.append(TaskCategoryFactory.create_category_from_configuration(sub_category_configuration))
        return categories
