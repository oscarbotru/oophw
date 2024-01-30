import json
import os


def read_json(path: str) -> dict:
    """Функция чтения json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        return data
