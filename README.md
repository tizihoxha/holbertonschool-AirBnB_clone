# AirBnB clone - The console
## Console
Console is a command line interpreter that manages the AirBnB objects. It takes input from the user one command at a time and interprets it. If it is error free then runs the command otherwise shows the error message.
### How to start/quit the console:
* To start interactive mode, use `./console.py`. (Non interactive mode `echo "help" | ./console.py`)
* To quit either type `quit` or `EOF`
### How to use the commands of the console:
* `help`: Provides documentation.
  *  Usage: `help`
* `all`: Prints all string representation of all instances based or not on the class name.
  * Usage: `all` or `all BaseModel`
* `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`.
  * Usage: `create BaseModel`
* `show`: Prints the string representation of an instance based on the class name and `id`.
  * Usage: `show BaseModel 1234-1234-1234`
* `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file).
  * Usage: `destroy BaseModel 1234-1234-1234`
* `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file).
  * Usage: `update BaseModel 1234-1234-1234 email "aibnb@mail.com"`


## Files
* [console.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/console.py) contains:
  * `Class HBNBCommand` with methods:
    * `def emptyline(self)` - handles emptyline.
    * `def do_quit(self, arg)` - exits the console.
    * `def do_create(self, arg)` - creates and saves a new instance and prints id.
    * `def do_show(self, arg)` - prints string representation of an instance base on classname and id.
    * `def do_destroy(self, arg)` - deletes an instance based on class name and id
    * `def do_all(self, arg)` - prints string representation of all instances/all instances of a class.
    * `def do_update(self, arg)` - uppdates instance based on class name and id by adding or updating attribute
* [base_model.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)
  * `Class BaseModel` with methods:
    * `def __init__(self, *args, **kwargs)` - initializes instance.
    * `def __str__(self)` - prints dictionary of attributes.
    * `def save(self)` - updates attribute `updated_at` with current datetime.
    * `def to_dict` - returns dictionary with all the keys and values of an instance with the class name it belongs to.
* [file_storage.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py) contains:
  * `class FileStorage` with methods:
    * `def all(self)` - returns __objects (class attribute).
    * `def new(self, obj)` - .sets obj in __objects with kkey/value pair.
    * `def save(self)` - serializes __objects to JSON file.
    * `def reload(self)` - deserializes JSON file to __objects.
* [user.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/user.py) contains:
  * `class User` with attributes:
    * `email` - empty string
    * `password` - empty string
    * `first_name` - empty string
    * `last_name` - empty string
* [city.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/city.py) contains:
  * `class City` with attributes:
    * `state_id` - empty string
    * `name` - empty string
* [state.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/state.py) contains:
  * `class State` with attributes:
    * `name` - empty string
* [place.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/place.py) contains:
  * `class Place` with attributes:
    * `city_id` - empty string
    * `user_id` - empty string
    * `name` - empty string
    * `description` - empty string
    * `number_rooms` - 0 (int)
    * `number_bathrooms` - 0 (int)
    * `max_guest` - 0 (int)
    * `price_by_night` - 0 (int)
    * `latitude` - 0.0 (float)
    * `longitude` - 0.0 (float)
    * `amenity_ids` - [] (empty list)
* [amenity.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/amenity.py) contains:
  * `class Amenity` with attributes:
    * `name` - empty string
* [review.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/review.py) contains:
  * `class Review` with attributes:
    * `place_id` - empty string
    * `user_id` - empty string
    * `text` - empty string


## Tests
Unittests are defined in `tests` folder. To run all the tests at once execute the command:
`python3 -m unittest`

* [test_base_model.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model.py)
* [test_file_storage.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py)
* [test_user.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_user.py)
* [test_amenity.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_amenity.py)
* [test_city.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_city.py)
* [test_place.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_place.py)
* [test_review.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_review.py)
* [test_state.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_state.py)
