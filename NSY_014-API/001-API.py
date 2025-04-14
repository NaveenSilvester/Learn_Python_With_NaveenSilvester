##################################################################################################
###                                 API
##################################################################################################
"""
An API (Application Programming Interface) is a set of protocols, tools and definitions that allow 
different software applications to communicate and interact with each other. APIs define how requests 
and responses should be formatted, making it easier to integrate various services or functionalities.

APIs serve as bridge, enabling developers integrate third-party functionalities or services into their 
own applications without having to build them from scratch. Essentially, APIs abstract the underlying 
complexity and provide simplified access to data, features, or services.

How does an API work?
    APIs typically operate via requests and responses:
    1.	Request: Your application sends a formatted request to the API with details about the desired action or data.
    2.	Processing: The API processes the request, interacts with its backend system, and fetches the relevant data or performs the task.
    3.	Response: The API send back a structured response, often in a format like JSON or XML, which your application can understand and use.

Types of APIs:
    Web APIs:
        •	Examples include RESTful APIs, SOAP, and GraphQL APIs.
        •	They allow interaction with web services over HTTP.
    Database APIs:
        •	Enable communication between applications and databases for data queries and modifications.
    Operating System APIs:
        •	Provide access to system-level resources like files, memory, and hardware.
    Library APIs:
        •	Found in programming libraries and frameworks, enabling modular development.

Key Concepts in APIs
1.	Endpoints: Specific URLs or routes where the API can receive requests
2.	Authentication: Mechanisms like API keys, OAuth tokens or JWTs for secure access.
3.	Rate Limits: Restrictions on the number of API request within a given timeframe
4.	Documentation: Comprehensive guides provided by the API’s creators to assist developers in understanding and using the API.

"""
print ("####################################################################################################")
print ("################################# Example-1: RESTful (requests method) #############################")
print ("####################################################################################################")

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # Print the list of posts

print ("####################################################################################################")

print ("####################################################################################################")
print ("################################# Example-2: RESTful (requests method) #############################")
print ("####################################################################################################")
print ("""
        Note: The example is a simple RESTful api where it tries fetch all the records of books from Books list
       and then also provides option to Add a book to the repository, fetch single book based on id and also delete 
       a book
       """)
print ("####################################################################################################")
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET a single book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

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
print ("####################################################################################################")

