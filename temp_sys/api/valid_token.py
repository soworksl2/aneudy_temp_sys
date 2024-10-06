from app import app


@app.route('/api/valid_token/<token>', methods=['GET'])
def valid_token(token: str) -> str:
    pass
