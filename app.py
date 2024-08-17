from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data (in-memory)
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Books API. Use /books to interact with the API."

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Get a book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        abort(404)
    return jsonify(book)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    new_book = {
        "id": books[-1]["id"] + 1 if books else 1,
        "title": request.json['title'],
        "author": request.json.get('author', "Unknown")
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update an existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book["id"] == id), None)
    if book is None:
        abort(404)
    if not request.json:
        abort(400)
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    return jsonify(book)

# Delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
