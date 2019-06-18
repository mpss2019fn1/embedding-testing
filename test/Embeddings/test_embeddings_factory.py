from src.Embeddings.embeddings_factory import EmbeddingsFactory
from test.base_test_case import BaseTestCase


class TestEmbeddingsFactory(BaseTestCase):

    def test_create_embeddings_from_file(self):
        file = self._random_test_file()
        file = file.with_suffix(EmbeddingsFactory.VALID_FILE_EXTENSION)
        with open(file, "w+") as file_output:
            print("1 3\nword -0.0762464299711 0.0128308048976 0.0712385589283", file=file_output)

        entity_linkings = EmbeddingsFactory.create_from_file(file)

        self.assertIsNotNone(entity_linkings["word"])

    def raise_exception_due_to_missing_header(self):
        file = self._random_test_file()
        file = file.with_suffix(EmbeddingsFactory.VALID_FILE_EXTENSION)
        with open(file, "w+") as file_output:
            print("word -0.0762464299711 0.0128308048976 0.0712385589283", file=file_output)

        self.assertRaises(AttributeError, EmbeddingsFactory.create_from_file, file)
