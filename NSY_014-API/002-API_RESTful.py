##################################################################################################
###                                 RESTful API
##################################################################################################
"""
RESTful APIs (Representational State Transfer)
REST is a popular architectural style used to build APIs. It relies on principles like statelessness, scalability, and simplicity.
Key Features:
•	Stateless: Every request is independent and does not rely on previous interactions.
•	Resource-Oriented: Resources are identified using URLs. Example: https://api.example.com/users
•	HTTP Methods:
o	GET: Retrieve data
o	POST: Create a new resource
o	PUT/PATCH: Update existing resources
o	DELETE: Remove resources
•	JSON Responses: REST APIs usually return data in JSON format, which is lightweight and human-readable.
How it works (Step by Step)
1.	The client sends an HTTP request to the API’s endpoint. Example: GET https://api.weather.com/city/Bengaluru
2.	The server processes the request and fetches the relevant data.
3.	A JSON response is returned to the client.

"""
print("###############################################################################################")
print ("############################# Example-1 (RESTFul API) ########################################")
print("###############################################################################################")
print("""
Note: A simple REST api which retrieves data from database using GET method,
      Searchers inividual record using a specific id by GET method
      Add's a record to the DB using POST method
      Deletes a record using Delete method.
      The Code uses flask module its methods like Flask, jsonify, requests
      """)
print("###############################################################################################")
print("""Code Ouput: Use Browser and use this url to check the outputs using the following endpoints:\n 
http://127.0.0.1:5000
      1. http://127.0.0.1:5000/books
      2. http://127.0.0.1:5000/books/multiple?ids=1,2,3
      
""")
from flask import Flask, jsonify, request
# Initiating Application

app = Flask(__name__)

# Creating a Sample Database
books = [
    {"id" : 1, "title" : "Python Programming", "Year" : "2024"},
    {"id" : 2, "title" : "Learn Python Programming with Naveen Silvester", "Year" : 2025}
]

# Setting Routes of the Page

# Fetch All the records from the database "books"

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Fetch a specific book from the databse "books"
@app.route('/books/multiple', methods=['GET'])
def get_multiple_books():
    # Get the 'ids' query parameter as a comma-separated string
    ids_param = request.args.get('ids')
    if not ids_param:
        return jsonify({"error": "Please provide a list of IDs as a query parameter (e.g., ?ids=1,2,3)"}), 400
    
    # Convert the string of IDs to a list of integers
    try:
        ids = list(map(int, ids_param.split(',')))
    except ValueError:
        return jsonify({"error": "Invalid IDs format. IDs must be integers separated by commas."}), 400
    
    # Filter books based on IDs
    selected_books = [book for book in books if book['id'] in ids]
    if not selected_books:
        return jsonify({"error": "No books found for the provided IDs."}), 404
    
    return jsonify(selected_books)


# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# DELETE a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

