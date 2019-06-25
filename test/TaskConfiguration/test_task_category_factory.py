import pytest

from src.Metric.cosine_similarity import CosineSimilarity
from src.Metric.euclidean_distance import EuclideanDistance
from src.Task import AnalogyTask, SimilarityTask
from src.TaskConfiguration import CategoryFileParser
from test.base_test_case import BaseTestCase


class TestTaskCategoryFactory(BaseTestCase):

    def test_create_categories_from_file(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"""
            configuration:
                categories:
                    - category:
                        name: category_name_1
                        enabled: true
                        tasks:
                            - task:
                                name: task_name_1
                                type: analogy
                                metric: cosine
                                test_set: {self.empty_file.absolute()}
                            - task:
                                name: task_name_2
                                type: similarity
                                metric: euclidean
                                test_set: {self.empty_file.absolute()}
                        categories:
                            - category:
                                name: sub_category_name_1
                                enabled: false
                                tasks:
                                categories:""",
                  file=file_output)

        categories = CategoryFileParser.create_categories_from_file(file)
        assert len(categories) == 1

        category = categories[0]
        assert category.name == "category_name_1"
        assert category.enabled
        assert len(category.tasks) == 2
        assert len(categories) == 1

    def test_extract_enabled(self):
        assert CategoryFileParser._extract_enabled({"enabled": "true"})
        assert CategoryFileParser._extract_enabled({"enabled": "TRUE"})

        assert not CategoryFileParser._extract_enabled({"enabled": "false"})
        assert not CategoryFileParser._extract_enabled({"enabled": "FALSE"})

    def test_extract_enabled_with_missing_key_raises_exception(self):
        config = {"invalid_key": "true"}
        with pytest.raises(KeyError):
            CategoryFileParser._extract_enabled(config)

    def test_extract_enabled_with_invalid_value_raises_exception(self):
        config = {"enabled": "not-a-boolean"}
        with pytest.raises(KeyError):
            CategoryFileParser._extract_enabled(config)

    def test_extract_name(self):
        config = {"name": "test-name"}
        assert CategoryFileParser._extract_name(config) == "test-name"

    def test_extract_name_with_missing_key_raises_exception(self):
        config = {"invalid_key", "test-name"}
        with pytest.raises(KeyError):
            CategoryFileParser._extract_name(config)

    def test_extract_name_with_empty_value_raises_exception(self):
        config = {"name": ""}
        with pytest.raises(KeyError):
            CategoryFileParser._extract_name(config)

    def test_extract_tasks(self):
        config = {
            "tasks": [
                {
                    "task": {
                        "name": "task-name-1",
                        "type": "analogy",
                        "metric": "cosine",
                        "test_set": str(self.empty_file.absolute())
                    }
                },
                {
                    "task": {
                        "name": "task-name-2",
                        "type": "similarity",
                        "metric": "euclidean",
                        "test_set": str(self.empty_file.absolute())
                    }
                }
            ]
        }

        tasks = CategoryFileParser._extract_tasks(config)
        assert len(tasks) == 2

        task = tasks[0]
        assert task.name == "task-name-1"
        assert task.__class__ == AnalogyTask
        assert task.metric == CosineSimilarity()
        assert task.test_set == self.empty_file

        task = tasks[1]
        assert task.name == "task-name-2"
        assert task.__class__ == SimilarityTask
        assert task.metric == EuclideanDistance()
        assert task.test_set == self.empty_file

    def test_extract_tasks_with_empty_list(self):
        config = {
            "tasks": None
        }

        tasks = CategoryFileParser._extract_tasks(config)
        assert len(tasks) == 0
