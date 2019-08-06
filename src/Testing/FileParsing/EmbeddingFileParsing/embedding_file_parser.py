import logging

from src.Testing.Embedding.embedding import Embedding
from src.Testing.FileParsing.abstract_file_parser import AbstractFileParser


class EmbeddingFileParser(AbstractFileParser):

    @staticmethod
    def create_from_file(file):
        from gensim.models import KeyedVectors

        if not file.exists() or not file.is_file():
            logging.error("Unable to locate embedding file")
            raise FileNotFoundError

        if not EmbeddingFileParser.header_is_present(file):
            logging.error("Provided file does not contain valid header")
            raise AttributeError

        return Embedding(KeyedVectors.load_word2vec_format(str(file)))

    @staticmethod
    def header_is_present(file):
        with file.open() as f:
            header_line = f.readline()
            f.seek(0)

        has_two_columns = len(header_line.split(" ")) == 2
        consists_only_of_digits = header_line.replace(" ", "").replace("\n", "").isdigit()

        return has_two_columns and consists_only_of_digits
