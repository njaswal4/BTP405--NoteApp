import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

# MySQL Connection Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'nj@mysql1',  
    'database': 'database1'   
}

# Function to connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(**mysql_config)

# Function to fetch all notes from the database
def get_all_notes():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    cursor.close()
    connection.close()
    return notes

# Function to create a new note in the database
def create_note(title, content):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    connection.commit()
    cursor.close()
    connection.close()

# Function to update an existing note in the database
def update_note(note_id, title, content):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (title, content, note_id))
    connection.commit()
    cursor.close()
    connection.close()

# Function to delete a note from the database
def delete_note(note_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    connection.commit()
    cursor.close()
    connection.close()

# HTTP request handler
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/notes':
            self.get_notes()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/notes':
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            self.create_note(post_data)
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        if self.path.startswith('/notes/'):
            note_id = int(self.path.split('/')[-1])
            content_length = int(self.headers['Content-Length'])
            put_data = json.loads(self.rfile.read(content_length))
            self.update_note(note_id, put_data)
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        if self.path.startswith('/notes/'):
            note_id = int(self.path.split('/')[-1])
            self.delete_note(note_id)
        else:
            self.send_response(404)
            self.end_headers()

    def get_notes(self):
        notes = get_all_notes()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(notes).encode())

    def create_note(self, data):
        create_note(data['title'], data['content'])
        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def update_note(self, note_id, data):
        update_note(note_id, data['title'], data['content'])
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def delete_note(self, note_id):
        delete_note(note_id)
        self.send_response(204)
        self.end_headers()

# Main function to run the server
def run():
    print('Starting server...')
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
