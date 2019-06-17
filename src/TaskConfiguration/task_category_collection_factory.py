import yaml

from src.TaskConfiguration import TaskCategoryCollection


class TaskCategoryCollectionFactory:
    LABEL_ROOT = "configuration"
    LABEL_CATEGORIES = "categories"
    LABEL_CATEGORY = "category"

    @staticmethod
    def create_configuration_from_file(configuration_file):
        from src.TaskConfiguration import TaskCategoryFactory

        with open(configuration_file, 'r') as stream:
            configuration = yaml.safe_load(stream)
        configuration = configuration[TaskCategoryCollectionFactory.LABEL_ROOT][
            TaskCategoryCollectionFactory.LABEL_CATEGORIES]
        categories = []
        for category in configuration:
            category = category[TaskCategoryCollectionFactory.LABEL_CATEGORY]
            categories.append(TaskCategoryFactory.create_category_from_configuration(category))

        return TaskCategoryCollection(categories)
