import pytest

from src.Embedding.embeddings_factory import EmbeddingsFactory
from test.base_test_case import BaseTestCase


class TestEmbeddingsFactory(BaseTestCase):

    def test_create_embeddings_from_file(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("1 3\n" +
                  "word -0.0762464299711 0.0128308048976 0.0712385589283", file=file_output)

        entity_linkings = EmbeddingsFactory.create_from_file(file)

        assert entity_linkings["word"] is not None

    def test_raise_exception_due_to_missing_header(self):
        file = self._random_test_file()
        with open(file, "w+") as file_output:
            print("word -0.0762464299711 0.0128308048976 0.0712385589283", file=file_output)

        with pytest.raises(AttributeError):
            EmbeddingsFactory.create_from_file(file)
