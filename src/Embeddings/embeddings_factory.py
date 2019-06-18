import logging
from pathlib import Path
from gensim.models import KeyedVectors

from src.Embeddings.embeddings import Embeddings


class EmbeddingsFactory:

    @staticmethod
    def create_from_file(file):
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
            header_line = f.readline()
            f.seek(0)

        has_two_columns = len(header_line.split(" ")) == 2
        consists_only_of_digits = header_line.replace(" ", "").replace("\n", "").isdigit()

        return has_two_columns and consists_only_of_digits
