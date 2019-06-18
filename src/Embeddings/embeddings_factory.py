import logging
from pathlib import Path
from gensim.models import KeyedVectors

from src.Embeddings.embeddings import Embeddings


class EmbeddingsFactory:

    VALID_FILE_EXTENSION = ".kv"

    @staticmethod
    def create_from_file(file: Path):
        if not file.exists() or not file.is_file():
            logging.error("Unable to locate embedding file")
            raise FileNotFoundError

        if not EmbeddingsFactory.header_is_present(file):
            logging.error("Provided file does not contain valid header")
            raise AttributeError

        return Embeddings(KeyedVectors.load_word2vec_format(str(file)))

    @staticmethod
    def header_is_present(file: Path):
        with file.open() as f:
            first_line = f.readline()
            f.seek(0)

        return len(first_line.split(" ")) == 2 and first_line.replace(" ", "").replace("\n", "").isdigit()
