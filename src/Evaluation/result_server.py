import pickle
from pathlib import Path
from typing import List

from flask import Flask, render_template

from src.Testing.Result.category_result import CategoryResult


class ResultServer:

    TEMPLATE_FOLDER = "__templates__"
    STATIC_FOLDER = "__static_files__"

    _results: List[CategoryResult] = []

    result_server = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)

    def __init__(self, results_file: Path):
        ResultServer._results = ResultServer._load_results(results_file)

    @staticmethod
    def _find_subtree_in_results(search_id, result_set):
        for test_category in result_set:
            if str(test_category.category.id) == search_id:
                return test_category
            sub_result = ResultServer._find_subtree_in_results(search_id, test_category.category_results)
            if sub_result:
                return sub_result
        return None

    @staticmethod
    def _load_results(result_file: Path) -> List[CategoryResult]:
        if not result_file.exists():
            raise FileNotFoundError(f"The given file {result_file} does not exist.")

        return pickle.load(result_file.open("rb"))

    @staticmethod
    @result_server.route('/', methods=['GET'])
    def index():
        return render_template('index.html', category_results=ResultServer._results)

    @staticmethod
    def run(debug: bool):
        ResultServer.result_server.run(debug)

    @staticmethod
    @result_server.route('/category/<search_id>', methods=['GET'])
    def category(search_id):
        selected_category = ResultServer._find_subtree_in_results(search_id, ResultServer._results)
        return render_template('category.html', results=ResultServer._results, selected_category=selected_category)
