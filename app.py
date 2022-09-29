from pathlib import Path
from typing import Iterable, Callable

from query_functions import file_to_generator, QueryPerformer

from flask import Flask, Response, request, abort

BASE_DIR: Path = Path(__file__).parent
DATA_DIR: Path = BASE_DIR.joinpath('data')

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    try:
        file_name: str = request.args['file_name']

        first_command: str = request.args['cmd1']
        first_value = request.args['value1']
        if first_command in ('map', 'limit'):
            first_value = int(first_value)

        second_command: str = request.args['cmd2']
        second_value = request.args['value2']
        if second_command in ('map', 'limit'):
            second_value = int(second_value)

        active_file: Iterable = file_to_generator(str(DATA_DIR.joinpath(file_name)))

        first_call: Callable = getattr(QueryPerformer, first_command)
        first_data_array: list = first_call(active_file, first_value)
        second_call: Callable = getattr(QueryPerformer, second_command)
        second_data_array: list = second_call(first_data_array, second_value)

        return app.response_class(second_data_array, content_type="text/plain")

    except (ValueError, FileNotFoundError):
        abort(400)


app.run()
