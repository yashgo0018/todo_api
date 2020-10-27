Todo API
===

## Installation
1. First Clone this repo.
2. Install All The dependencies `pip install -r requirements.txt`
3. Create All The Database Tables `python manage.py migrate`
4. Start The Server `python manage.py runserver`
Then you are all done.

Now You may test you the routes
1. POST -> `/todos/` with data `{"title": "string", "notes": "string"}`
2. GET -> `/todos/` to get all the tods
3. GET -> `/todos/{id}` to get the todo of that id