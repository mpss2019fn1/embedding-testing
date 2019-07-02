from flask import Flask, render_template

TEMPLATE_FOLDER = "__templates__"
STATIC_FOLDER = "__static_files__"

result_server = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


@result_server.route('/', methods=['GET'])
def index():
    result_set = result_server.config.get("results")
    return render_template('index.html', category_results=result_set)


@result_server.route('/category/<search_id>', methods=['GET'])
def category(search_id):
    result_set = result_server.config.get("results")
    selected_category = _find_subtree_in_results(search_id, result_set)
    return render_template('category.html', results=result_set, selected_category=selected_category)


def _find_subtree_in_results(search_id, result_set):
    for test_category in result_set:
        if str(test_category.category.id) == search_id:
            return test_category
        sub_result = _find_subtree_in_results(search_id, test_category.category_results)
        if sub_result:
            return sub_result
    return None
