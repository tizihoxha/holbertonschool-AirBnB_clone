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
* [console.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/console.py)
* [base_model.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/base_model.py)
* [file_storage.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py)
* [user.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/user.py)
* [city.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/city.py)
* [state.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/state.py)
* [place.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/place.py)
* [amenity.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/amenity.py)
* [review.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/models/review.py)

## Tests
* [test_base_model.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model.py)
* [test_file_storage.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py)
* [test_user.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_user.py)
* [test_amenity.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_amenity.py)
* [test_city.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_city.py)
* [test_place.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_place.py)
* [test_review.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_review.py)
* [test_state.py](https://github.com/tizihoxha/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_state.py)
