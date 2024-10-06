from os import path
from io import TextIOBase


class TokensManager:
    def __init__(self, tokens_file: str) -> None:
        self.tokens_file: str = tokens_file
        self.tokens: list[str] = []
        self.tokens_last_modify: float = 0

        self._ensure_file()
        self._reload_tokens()

    def _open_tokens(self) -> TextIOBase:
        return open(self.tokens_file, 'w')

    def _ensure_file(self) -> None:
        if not path.exists(self.tokens_file):
            with self._open_tokens():
                pass

    def _reload_tokens(self) -> None:
        with self._open_tokens() as f:
            raw_tokens: list[str] = f.readlines()
            self.tokens = []
            for raw_token in raw_tokens:
                self.tokens.append(raw_token.strip())
            self.tokens_last_modify = path.getmtime(self.tokens_file)

    def _need_reload_tokens(self) -> bool:
        tokens_current_modify: float = path.getmtime(self.tokens_file)

        return tokens_current_modify > self.tokens_last_modify

    def exists(self, token: str) -> bool:
        if self._need_reload_tokens():
            self._reload_tokens()

        return token in self.tokens
