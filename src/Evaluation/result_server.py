from flask import Flask, render_template

TEMPLATE_FOLDER = "__templates__"
STATIC_FOLDER = "__static_files__"

result_server = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)


@result_server.route('/', methods=['GET'])
def student():
    return render_template('index.html', result={})
