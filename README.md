# AirBnB clone - The console #

<img src='https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67' alt='HBnB'/>

## _Introduction_ 📢

**The AirBnb Clone project console** serves as a versatile developer tool designed for efficient management of objects and data through a command-line interface (CLI). It offers a range of functionalities including creating, updating, destroying, and displaying objects/data. One of its key features is the seamless storage and persistence of objects to a JSON file. This tool is instrumental in abstracting the interaction between the storage engine and object/data management, thereby providing flexibility to easily switch between different storage types.

The primary objective of this project is to develop a _data model, a command interpreter, and a JSON file storage system_. When these components are integrated, they enable users to effectively maintain the file storage engine while executing various operations on the objects stored within the system, all through a user-friendly CLI.

## _The flowchart of the Program_ ⚡

<a href="https://ibb.co/yYQDtXh"><img src="https://i.ibb.co/KLrYdXN/flowchart-console.png" alt="flowchart-console" border="0"></a>

## _The file structure_ 📔

<a href="https://ibb.co/WFDpRFw"><img src="https://i.ibb.co/Y8DTV8M/file-structure.png" alt="file-structure" border="0"></a>

## _Description_ ✍

* __BaseModel__
defines common attributes and methods for every other data field class
    - `__init__`: constructor for BaseModel instances
        - `id`: instance id in uuid4 format
        - `created_at`: datetime object attribute initialized at instantiation
        - `updated_at`: datetime object attribute initialized at instantiation
    - `__str__`: object string representation
    - `save()`: updates the public instance attribute `updated_at` with the current datetime
    - `to_dict()`: returns a dictionary containing all keys/values of `__dict__` of the instance:

* __FileStorage__
defines attributes and methods for serializing Python objects into JSON file, and deserializing JSON string into Python objects
    - `__file_path`: path to the JSON storage file
    - `__objects`: dictionary that maps Classname.ID
    - `all()`: returns the `__objects` dictionary
    - `new()`: adds a new object to the `__objects` dictionary
    - `save()`: serializes `__objects` to the JSON file
    - `reload()`: deserializes the JSON file to `__objects`

* __Console__
contains the definition for a command line interpeter. The functionality of this CLI includes: creating new instances of data objects, showing data stored in a file storage engine, deleting and updating instances

* __Data Fields(User, State, City, Amenity, Place, Review, State)__
classes inherting from BaseModel and defining their public class attributes
    - __User__:
        - `email`
        - `password`
        - `first_name`
        - `last_name`
    - __State__:
        - `name`
    - __City__:
        - `state_id`
        - `name`
    - __Amenity__:
        - `name`
    - __Place__:
        - `city_id`
        - `user_id`
        - `name`
        - `description`
        - `number_rooms`
        - `number_bathrooms`
        - `max_guest`
        - `price_by_night`
        - `latitude`
        - `longitude`
        - `amenity_ids`
    - __Review__:
        - `place_id`
        - `user_id`
        - `text`

## _Execution_ 🔐

The shell should look like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

And also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## _Implementation of the commands_ 🛠

- `create` - creates a new instance of BaseModel, saves it to the JSON file and prints id

```
(hbnb) create
** class name missing **
(hbnb) create MyModel
** class doesn't exist **
(hbnb) create BaseModel
354181fe-97d1-4cb3-b4c6-19277af3d982
```

- `show` - prints string representation of an instance based on the class name

```
(hbnb) show
** class name missing **
(hbnb) show BaseModel
(hbnb) show MyModel
** class doesn't exist **
** instance id missing **
(hbnb) show BaseModel 354181fe-97d1-4cb3-b4c6-19277af3d982
[BaseModel] (354181fe-97d1-4cb3-b4c6-19277af3d982) {'id': '354181fe-97d1-4cb3-b4c6-19277af3d982', 'created_at': datetime.datetime(2023, 10, 9, 11, 16, 1, 910572), 'updated_at': datetime.datetime(2023, 10, 9, 11, 16, 1, 910589)}
```

- `destroy` - deletes an instance based on the class name and id

```
(hbnb) destroy
** class name missing **
(hbnb) destroy MyModel
** class doesn't exist **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 354181fe-97d1-4cb3-b4c6-19277af3d982
(hbnb) show BaseModel 354181fe-97d1-4cb3-b4c6-19277af3d982
** no instance found **
```

- `all` - prints string representation of all instances based or not on the class name

```
(hbnb) all
["[BaseModel] (3ddf7693-16a7-41da-8e24-b8395ad6506f) {'id': '3ddf7693-16a7-41da-8e24-b8395ad6506f', 'created_at': datetime.datetime(2023, 10, 9, 11, 10, 10, 751048), 'updated_at': datetime.datetime(2023, 10, 9, 11, 10, 10, 751101)}"]
(hbnb) all BaseModel
["[BaseModel] (3ddf7693-16a7-41da-8e24-b8395ad6506f) {'id': '3ddf7693-16a7-41da-8e24-b8395ad6506f', 'created_at': datetime.datetime(2023, 10, 9, 11, 10, 10, 751048), 'updated_at': datetime.datetime(2023, 10, 9, 11, 10, 10, 751101)}"]
```

- `update` - updates an instance based on the class name and id by adding or updating attribute

```
(hbnb) update BaseModel 3ddf7693-16a7-41da-8e24-b8395ad6506f first_name "Betty"
(hbnb) show BaseModel 3ddf7693-16a7-41da-8e24-b8395ad6506f
[BaseModel] (3ddf7693-16a7-41da-8e24-b8395ad6506f) {'id': '3ddf7693-16a7-41da-8e24-b8395ad6506f', 'created_at': datetime.datetime(2023, 10, 9, 11, 10, 10, 751048), 'updated_at': datetime.datetime(2023, 10, 9, 11, 10, 10, 751101), 'first_name': '"Betty"'}
```

## _Testing_ 📋

All files, classes and functions are tested with unit tests. 

The tests can be executed by using the command  `python3 -m unittest discover tests`

Also the tests can be executed file by file, e.g. `python3 -m unittest tests/test_models/test_base_model.py`, `python3 -m unittest tests/test_models/test_engine/test_file_storage.py` etc.

The tests should also pass in non-interactive mode using the command `echo "python3 -m unittest discover tests" | bash`

## _Authors_ ✍ 

Chris Stephens <6673@holbertonstudents.com><br />
Svitlana Pavlovska <lanapavlovska90@gmail.com>
