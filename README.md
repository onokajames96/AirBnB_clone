# AirBnB clone
AirBnB clone

writing  a command line interpreter.
This is the first step towards building your first full web application: the AirBnB clone.

The goal of the project is to deploy on your server a simple copy of the AirBnB website.

# Concepts to learn
Unittest - and please work all together on tests cases
Python packages concept page
Serialization/Deserialization
*args, **kwargs
datetime
More coming soon

# You won’t build this application all at once, but step by step.

Each step will link to a concept:
# The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)

# Web static
learn HTML/CSS
create the HTML of your application
create template of each object

# MySQL storage
replace the file storage by a Database storage
map your models to a table in database by using an O.R.M.

# Web framework - templating
create your first web server in Python
make your static HTML file dynamic by using objects stored in a file or database

# RESTful API
expose all your objects stored via a JSON web interface
manipulate your objects via a RESTful API

# Web dynamic
learn JQuery
load objects from the client side by using your own RESTful API

# Files and Directories
models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

