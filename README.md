# Book API with Flask

This repository contains the design, implementation, documentation, and interaction of a RESTful API using Python and Flask.

## Features

- **API Endpoints**:
  - `GET /books`: Retrieve all books.
  - `GET /books/<id>`: Retrieve a book by its ID.
  - `POST /books`: Add a new book.
  - `PUT /books/<id>`: Update a book by its ID.
  - `DELETE /books/<id>`: Delete a book by its ID.

## Setup

1. **Activate Environment**:
   ```bash
   conda activate env_name
   ```

2. **Create the API**:
   - Implementation in `app.py`.

3. **Run the API**:
   ```bash
   python app.py
   ```
   - Access at `http://127.0.0.1:5000/`.

## Interacting with the API

- **Add a New Book**:
  ```bash
  curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title": "Brave New World", "author": "Aldous Huxley"}'
  ```

- **Update a Book**:
  ```bash
  curl -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"title": "1984", "author": "George Orwell Updated"}'
  ```

- **Delete a Book**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/books/1
  ```

## Documentation

- API documentation can be found in `document.md`.

## Deploying with Docker

1. **Create Dockerfile**.
2. **Create `requirements.txt`**.
3. **Build the Docker Image**:
   ```bash
   docker build -t book_api .
   ```
4. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 book_api
   ```
5. **Access the API**:
   - `http://127.0.0.1:5000/`

<!-- ## Develop for Web and Mobile

- Details for web and mobile platform development are included. -->

