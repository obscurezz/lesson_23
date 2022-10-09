from re import search
from typing import Iterable


def file_to_generator(filename: str) -> Iterable:
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            try:
                row = next(file)
                yield row
            except StopIteration:
                break


class QueryPerformer:
    @staticmethod
    def filter(data_array: Iterable, input_string: str) -> list:
        return list(filter(lambda x: input_string in x, data_array))

    @staticmethod
    def map(data_array: Iterable, col_number: int) -> list:
        return list(map(lambda x: x.split()[col_number], data_array))

    @staticmethod
    def unique(data_array: Iterable, empty_value: None = None) -> list:
        return list(set(data_array))

    @staticmethod
    def sort(data_array: Iterable, order: str) -> list:
        return sorted(data_array, reverse=True) if order == 'desc' else sorted(data_array)

    @staticmethod
    def limit(data_array: Iterable, count: int) -> list:
        return list(data_array)[:count]

    @staticmethod
    def regex(data_array: Iterable, reg_expression: str) -> list:
        result: list = [row for row in data_array if search(rf'{reg_expression}', row)]
        return result
