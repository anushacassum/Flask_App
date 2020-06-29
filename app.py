from flask import Flask, jsonify, request, Response
import json
from settings import *


books = [
	{
		'name': 'Green Eggs and Ham',
		'price': 7.99,
		'isbn': 327817192
	},
	{
		'name': 'The Cat in the Hat',
		'price': 8.99,
		'isbn': 274847291
	}
]

#GET /store
@app.route('/books')
def hello_world():
	return jsonify({'books': books})

def validBookObject(bookObject):
	if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
		return True
	else:
		return  False


@app.route('/books', methods=['POST'])
def add_book():

	request_data = request.get_json()
	print(type(request_data))
	if (validBookObject(request_data)):
		new_book = {
			"name": request_data['name'],
			"price": request_data['price'],
			"isbn": request_data['isbn']
		}
		books.insert(0, new_book)
		response = Response("", 201, mimetype='application/json')
		response.headers['Location'] = "/books/" + str(new_book["isbn"])
		return response
	else:
		invalidBookObjectErrorMsg = {
			"error": "Invalid book object passed in request",
			"helpString": "Data passed in similar to this {'name': 'bookname', 'price': 7.99, 'isbn': 937284937}"
		}
		response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json');
		return response


#GET /books/274847291
@app.route('/books/<int:isbn>')
def get_books_by_isbn(isbn):
	return_value = {}
	for book in books:
		if book['isbn'] == isbn:
			return_value = {
				'name': book['name'],
				'price': book['price']
			}
	return jsonify(return_value)


#PUT
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
	request_data = request.get_json()
	new_book = {
		'name': request_data['name'],
		'price': request_data['price'],
		'isbn': isbn
	}
	i= 0;
	for book in books:
		if book['isbn'] == isbn:
			books[i] = new_book
		i += 1
	response = Response("", status=204)
	return response


@app.route('/books/<int:isbn>', methods=['PATCH'])
def update_book(isbn):
	request_data = request.get_json()
	updated_book = {}
	if ("name" in request_data):
		updated_book["name"] = request_data["name"]
	if ("price" in request_data):
		updated_book["price"] = request_data["price"]
	for book in books:
		if book['isbn'] == isbn:
			book.update(updated_book)
	response = Response("", status=204)
	response.headers['Location'] = "/books/" + str(isbn)
	return response


@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
	i = 0;
	for book in books:
		if book["isbn"] == isbn:
			books.pop(i)
		i += 1
	return "";

app.run(port=5000)
