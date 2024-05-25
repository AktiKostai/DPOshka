from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/books/<int:id>')
def get_book(id):
    book = {
        "id": id,
        "title": "Metro 2033",
        "publication_date": "October 2010",
        "publisher": "Glux",
        "isbn": "9871789959384"
    }
    return jsonify(book)


@app.route('/hello')
def hello():
    return "Hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
