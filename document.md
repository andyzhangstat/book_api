# Books API

## Endpoints

### GET /books
- **Description**: Retrieve a list of all books.
- **Response**:
  - `200 OK` - Returns a JSON array of all books.

### GET /books/<id>
- **Description**: Retrieve a specific book by its ID.
- **Parameters**:
  - `id` (integer) - The ID of the book.
- **Response**:
  - `200 OK` - Returns the book with the specified ID.
  - `404 Not Found` - If the book is not found.

### POST /books
- **Description**: Add a new book.
- **Request Body** (JSON):
  - `title` (string, required) - The title of the book.
  - `author` (string, optional) - The author of the book.
- **Response**:
  - `201 Created` - Returns the newly created book.
  - `400 Bad Request` - If the request body is invalid.

### PUT /books/<id>
- **Description**: Update an existing book by its ID.
- **Parameters**:
  - `id` (integer) - The ID of the book.
- **Request Body** (JSON):
  - `title` (string, optional) - The updated title of the book.
  - `author` (string, optional) - The updated author of the book.
- **Response**:
  - `200 OK` - Returns the updated book.
  - `400 Bad Request` - If the request body is invalid.
  - `404 Not Found` - If the book is not found.

### DELETE /books/<id>
- **Description**: Delete a book by its ID.
- **Parameters**:
  - `id` (integer) - The ID of the book.
- **Response**:
  - `204 No Content` - If the book is successfully deleted.
  - `404 Not Found` - If the book is not found.
