from src.TaskConfiguration import TaskCategoryCollectionFactory
from test.base_test_case import BaseTestCase


class TestTaskCategoryCollectionFactory(BaseTestCase):

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

        categories = TaskCategoryCollectionFactory.create_categories_from_file(file)
        self.assertEqual(1, len(categories.categories))

        category = categories.categories[0]
        self.assertEqual("category_name_1", category.name)
        self.assertTrue(category.enabled)
        self.assertEqual(2, len(category.tasks))
        self.assertEqual(1, len(category.categories))
