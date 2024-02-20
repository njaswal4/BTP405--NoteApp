
This project provides a simple backend for a note-taking application, built using Python and MySQL. 
The backend offers a RESTful API allowing users to perform CRUD operations (Create, Read, Update, Delete) on notes stored in a MySQL database. 
To run the application, ensure you have Python, MySQL, and Docker installed on your system. After cloning the repository, navigate to the
 project directory and build the Docker containers using the provided docker-compose.yml file (docker-compose up --build).
 Once the containers are up and running, you can access the API endpoints to manage notes. 
 The API includes endpoints for retrieving all notes (GET /notes) and creating new notes (POST /notes).
 To test the API endpoints, you can use tools like Postman or cURL. For example, to retrieve all notes, 
 you can send a GET request to http://localhost:8000/notes.
 Detailed instructions and example responses are provided in the sections below. 
 Please ensure Docker and Docker Compose are installed on your system before running the application.

 API Endpoints
 -------------
GET /notes
Retrieves all notes from the database.

Method: GET
Example Response:
json
Copy code
[
  {
    "id": 1,
    "title": "Note 1",
    "content": "hello!"
  },
  {
    "id": 2,
    "title": "Note 2",
    "content": "This is a new note"
  }
]
POST /notes
Creates a new note.

Method: POST
Request Body:
json
Copy code
{
  "title": "New Note",
  "content": "This is a new note"
}
Testing the API Endpoints
You can test the API endpoints using tools like Postman or cURL. For example:

To retrieve all notes:
bash
Copy code
curl http://localhost:8000/notes

POST /notes: Create a new note
Example:
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Note", "content": "This is a new note."}' http://localhost:8000/notes

PUT /notes/{note_id}: Update an existing note
Example:
curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Note", "content": "This note has been updated."}' http://localhost:8000/notes/1

DELETE /notes/{note_id}: Delete a note by ID
Example:
curl -X DELETE http://localhost:8000/notes/1