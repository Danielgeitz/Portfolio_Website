# Start venv: venv\Scripts\activate.bat
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


# Error Pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
