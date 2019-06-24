from src.Embedding.embedding_factory import EmbeddingFactory
from src.EntityLinking.entity_linkings_factory import EntityLinkingsFactory
from src.Metric.cosine_similarity import CosineSimilarity
from src.Task import SimilarityTask, TaskType
from src.TaskConfiguration import TaskConfiguration
from src.TestConfiguration.test_configuration import TestConfiguration
from test.base_test_case import BaseTestCase


class TestSimilarityTask(BaseTestCase):

    def test_run(self):
        test_set_file = self._random_test_file()
        with open(test_set_file, "w+") as file_output:
            print("a,b,is_similar\n" +
                  "wd:Q567,wd:Q71359,true\n" +
                  "wd:Q9671,wd:Q567,false", file=file_output)

        linking_file = self._random_test_file()
        with open(linking_file, "w+") as file_output:
            print("embedding_label,knowledge_base_id\n" +
                  "angela_merkel,wd:Q567\n" +
                  "michael_schumacher,wd:Q9671\n" +
                  "akk,wd:Q71359", file=file_output)

        embedding_file = self._random_test_file()
        with open(embedding_file, "w+") as file_output:
            print("3 2\n" +
                  "angela_merkel 2.0 2.0\n" +
                  "akk 4.0 3.8\n" +
                  "michael_schumacher -1.25 -32.0", file=file_output)

        entity_linking = EntityLinkingsFactory.create_from_file(linking_file)
        embedding = EmbeddingFactory.create_from_file(embedding_file)
        task_configuration = TaskConfiguration(TaskType.SIMILARITY, True)

        test_config = TestConfiguration(embedding, entity_linking, [], [task_configuration])

        similarity_task = SimilarityTask("Similarity Task", test_set_file, CosineSimilarity())
        task_result = similarity_task.run(test_config)

        assert 2 == len(task_result.case_results)
        assert 100 == task_result.pass_rate()
        assert 0 < task_result.execution_duration()
        assert task_result.case_results[0].expected_output
        assert not task_result.case_results[1].expected_output