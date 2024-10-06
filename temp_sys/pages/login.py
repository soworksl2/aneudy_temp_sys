from flask import render_template

from app import app


@app.route('/login')
def login() -> str:
    return render_template('login.html')
