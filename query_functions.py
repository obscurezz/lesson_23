from typing import Iterable


def file_to_generator(filename: str):
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
    def unique(data_array: Iterable, empty_value=None) -> list:
        return list(set(data_array))

    @staticmethod
    def sort(data_array: Iterable, order: str) -> list:
        if order == 'asc':
            return sorted(data_array)
        elif order == 'desc':
            return sorted(data_array, reverse=True)

    @staticmethod
    def limit(data_array: Iterable, count: int) -> list:
        return list(data_array)[:count]
