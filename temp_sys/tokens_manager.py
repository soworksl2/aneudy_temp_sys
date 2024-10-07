from os import path
from io import TextIOBase

from typing import Literal


class TokensManager:
    def __init__(self, storage_dir: str) -> None:
        self.storage_dir: str = storage_dir

        self._ensure_storage_dir()

    def _ensure_storage_dir(self) -> None:
        if not path.isdir(self.storage_dir):
            raise Exception(f'storage_dir "{self.storage_dir}" does not exists')

    def exists(self, token: str) -> bool:
        possible_token_file: str = path.join(self.storage_dir, token + '.json')
        return path.isfile(possible_token_file)
