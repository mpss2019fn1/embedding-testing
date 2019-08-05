import pytest

from src.Testing.EntityLabel.entity_labels import EntityLabels
from src.Testing.FileParsing.ConfigurationFileParsing.task_category_file_parser import TaskCategoryFileParser
from src.Testing.Task.Analogy.analogy_task import AnalogyTask
from src.Testing.Task.Similarity.cosine_similarity_task import CosineSimilarityTask
from test.Testing.base_test_case import BaseTestCase


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
                                test_set: {self.empty_file.absolute()}
                            - task:
                                name: task_name_2
                                type: cosine_similarity
                                test_set: {self.empty_file.absolute()}
                        categories:
                            - category:
                                name: sub_category_name_1
                                enabled: false
                                tasks:
                                categories:""",
                  file=file_output)

        entity_labels = EntityLabels()
        categories = TaskCategoryFileParser.create_categories_from_file(file, entity_labels)
        assert len(categories) == 1

        category = categories[0]
        assert category.name == "category_name_1"
        assert category.enabled
        assert len(category.tasks) == 2
        assert len(categories) == 1

        task = category.tasks[0]
        assert task.name == "task_name_1"
        assert task.__class__ == AnalogyTask
        assert task.test_set == self.empty_file

        task = category.tasks[1]
        assert task.name == "task_name_2"
        assert task.__class__ == CosineSimilarityTask
        assert task.test_set == self.empty_file

        subcategory = category.categories[0]
        assert subcategory.name == "sub_category_name_1"
        assert not subcategory.enabled
        assert len(subcategory.tasks) == 0
        assert len(subcategory.categories) == 0

    def test_create_from_file_empty_categories(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"""
            configuration:
                categories:""", file=file_output)

        entity_labels = EntityLabels()
        categories = TaskCategoryFileParser.create_categories_from_file(file, entity_labels)
        assert len(categories) == 0

    def test_enabled_is_not_a_boolean(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"""
                    configuration:
                        categories:
                            - category:
                                name: category_name_1
                                enabled: not_a_boolean
                                tasks:
                                categories:""",
                  file=file_output)

        with pytest.raises(KeyError):
            entity_labels = EntityLabels()
            categories = TaskCategoryFileParser.create_categories_from_file(file, entity_labels)

    def test_enabled_is_missing(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"""
                    configuration:
                        categories:
                            - category:
                                name: category_name_1
                                tasks:
                                categories:""",
                  file=file_output)

        with pytest.raises(KeyError):
            entity_labels = EntityLabels()
            categories = TaskCategoryFileParser.create_categories_from_file(file, entity_labels)

    def test_name_is_empty(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"""
                    configuration:
                        categories:
                            - category:
                                name: 
                                enabled: not_a_boolean
                                tasks:
                                categories:""",
                  file=file_output)

        with pytest.raises(KeyError):
            entity_labels = EntityLabels()
            categories = TaskCategoryFileParser.create_categories_from_file(file, entity_labels)

    def test_name_is_missing(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print(f"""
                    configuration:
                        categories:
                            - category:
                                enabled: not_a_boolean
                                tasks:
                                categories:""",
                  file=file_output)

        with pytest.raises(KeyError):
            entity_labels = EntityLabels()
            categories = TaskCategoryFileParser.create_categories_from_file(file, entity_labels)
