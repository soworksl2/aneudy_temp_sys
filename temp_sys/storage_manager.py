from os import path

from temp_sys.tokens_manager import TokensManager


STORAGE_DIR: str = 'db'
TOKENS_FILENAME: str = 'tokens.txt'
TOKENS_FILE_PATH: str = path.join(STORAGE_DIR, TOKENS_FILENAME)


tokens: TokensManager = TokensManager(TOKENS_FILE_PATH)
