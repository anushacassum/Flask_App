def validBookObject(bookObject):
	if ("price" in bookObject and "name" in bookObject and "isbn" in bookObject):
		return True
	else:
		return  False

valid_object = {
	"name": "Minnie Mouse and the house",
	"price": 3.99,
	"isbn": 72781828
}

missing_name= {
	"price": 3.99,
	"isbn": 72781828
}

