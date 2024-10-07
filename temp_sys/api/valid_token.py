from flask import Response

from app import app
from temp_sys.storage_manager import tokens


@app.route('/api/valid_token/<token>', methods=['GET'])
def valid_token(token: str) -> Response:
    exists: bool = tokens.exists(token)
    status: int = 200 if exists else 404
    return Response(status=status)
