from pathlib import Path
from dacite import from_dict
from typing import Iterable, Callable

from commands import Commands
from flask import Flask, Response, request, abort

from query_functions import file_to_generator, QueryPerformer

BASE_DIR: Path = Path(__file__).parent
DATA_DIR: Path = BASE_DIR.joinpath('data')

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    try:
        commands: Commands = from_dict(data_class=Commands, data=request.args)
        active_file: Iterable = file_to_generator(str(DATA_DIR.joinpath(commands.file_name)))

        first_call: Callable = getattr(QueryPerformer, commands.cmd1)
        first_data_array: list = first_call(active_file, commands.value1)

        second_call: Callable = getattr(QueryPerformer, commands.cmd2)
        second_data_array: list = second_call(first_data_array, commands.value2)

        return app.response_class(second_data_array, content_type="text/plain")

    except (ValueError, FileNotFoundError) as e:
        abort(400, e)


app.run()
