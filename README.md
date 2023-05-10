## <span style="color:blue">Casting agency</span>
-----------------
Casting agency application can be used to store actors and movies data.
This Final Project demonstrates skills in:
- Coding in Python 3
- Relational Database Architecture
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access
- Authentication with Auth0
- Authentication in Flask
- Role-Based Access Control (RBAC)
- Testing Flask Applications
- Deploying Applications

## Project Dependencies:

Recommended to use virtual environment.

Python 3.11

PostgreSQL

To install required packages for python:

    pip3 install -r requirements.txt

Start the postgresql server on ubuntu:

    sudo service postgresql start

Now we need to create main and test databases:

    sudo -u postgres createdb casting_agency

    sudo -u postgres createdb casting_agency_test

Psql users and passwords can be edited in the .env file.

Locally, the application will run on <a href="localhost:5000/">localhost:5000/</a>


#### Start the development server

From the main folder with app.py file run the command on Lunix:

    export FLASK_APP=app && export FLASK_ENV=development && flask run --reload

On Windows:

    set FLASK_APP=app
    set FLASK_ENV=development
    set flask run --reload

## Authentication
_____________________

For the login purposes this app is using 3d party authentication: Auth0 services.
To work with routes, you will need jwt tokens presented below.

## <span style="color:blue">Roles</span>
----------
There are 3 roles:

#### Casting Assistant

- Can view actors and movies

#### Casting Director

- All permissions for Casting Assistant
- Add or delete an actor from the database
- Modify actors or movies

#### Executive Producer

- All permissions for Casting Director
- Add or delete a movie from the database

## JWT information
________________

casting_assistant_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2IxNjVlZjliMjUxOTE1OTM4YzIiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzU0MTQ0NCwiZXhwIjoxNjgzNjI3NDQ0LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIl19.yQFzCSDbvByoadY5d7Yj1qMXlD760imBmdbFXqZOFXWa_iH_YPoi8PBlQNpHQ3Lk96w5wwA9DFlUuoDbtGk20jZlGuwBqPvWoPRGTeWpWiisf59L79DHweFADqTfeFGlDsx5A4lNou_yltdLBkKGH7sW3QQ6Y1WvJMAbQDKdtZVkapnjqhQdF4IVDdXXiVe3Alqnwxpx7dkvtberKSiKVHarSzCwimPv_Bo78Dtmzh8t1hbUcsh2yIsLw0nCBCL2J0Ij5k2tPJ3kWTVB64e5xBe2pr9INN6FLx0VE2rpJFlpRNb6XOee7Rgdlku_x1FiEg61s0U1ERYpjzbaqOTSug

casting_director_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2I3ZTc4YjAzZTYxZDZjMjQyOWEiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzU0MTU4MCwiZXhwIjoxNjgzNjI3NTgwLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.As5k0z356iSaXIR5yxvFoIzIk0LYjuZc-FDOj4zQqeLR67JJJDjIuMvD8ZHXVshQ0Gpj_-igiDCkVN-UZBZcXo86oZZzyHUAQIw9W9lKppWUyo-hCC2whI8QVxan4EMKS0_xUeoz2GwbKLTNQjJOfvxu0DRoGp7BHHwz_SHWgxsCFlQ3xiWXBccMRZkfbI0Bd8PGgkj9lmoXpDy6WqtLFaMX2tMiyW2LFPOGRrIFaKrXe8LW5dnqXivFObXb_c9oziGik_-MERBJ9Vu36-HZo3uP7zczKQ3gS-XciLTRaGAszkL8efZtMiXRCk2RgoHmp9mqyI5X1WZ_6AwBwOJc4w

executive_producer_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRlN2M3Yzc4YjAzZTYxZDZjMWVhM2EiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzU0MTY3NSwiZXhwIjoxNjgzNjI3Njc1LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.7rRJBi7gOYduF8Oyy0KLYQaXe8stqRNwQkdAnsObgBg39OUKbip1rJcFDiD-AU0aLcsfUlViXxX4h-7xnPXrEOb-og33qX-_3RNVYFCBeMP1ro9I9RmjD-6aPs50v_EdArodeKGwp34yIOWSfWrFoyXwS1pz3nD6b5wcTKHbjxlQpNLX3jnJSUviRSOKPqtxraasK7G0d5uKdY66G58HURNaZU-FJP9LFF1a9UaC5d6h1zBNhfKpKvnG_3H7K4zw9kd8HrtPwr4oVYURlEvLm7KX3ASWF99LJ31lkmv3wIbM0keS1Ssb03Z9713or39CX2Kd-tc49-4-FZluI17vaw




## <span style="color:blue"> Routes </span>

### / methods = GET
_______________________________________________
Main page.

Response:

        "Home page"


### /movies and /actors, methods = GET
_______________________________________________

JSON response:

        {
            "success": True,
            "movies": movies_list // "actors": actors_list
        }


### - /movies/id and /actors/id, methods = GET
________________________________________

JSON response:

        {
           "success": True,
           "movie_info": movie.get_details() // "actor_info": actor.get_details()
        }


### - /movies/id and /actors/id, methods = PATCH
_______________________________________

JSON response:

        {
          "success": True,
          "movie": movie.get_details() // "actor": actor.get_details()
        }


### - /movies and /actors, methods = POST
_________________________________________

JSON response:

        {
          "success": True,
          "movie": movie.get_details() // "actor": actor.get_details()
        }

### - /movies/id and /actors/id, methods = DELETE
_________________________________________

JSON response:

        {
          "success": True,
          "deleted": movie.id // "deleted": actor.id
        }


## <span style="color:blue"> ERRORS </span>

**Auth0 errors**: token_expired, invalid_claims, invalid_header.

**Application** errors:
- 400:Bad Request. The server couldn't process your request,
- 404:You are trying to access an item that is not in the database.
The server can not find the requested resource.,
- 422:The request was well-formed but was unable to be followed due to semantic errors. The server couldn't process your request.


## <span style="color:blue"> Tests </span>

Testing is done with unittest library, to run the tests:

    psql -u postgres casting_agency_test < casting_agency_test.bak

    python test_app.py

Tests check all endpoints for success and fail behaviors, as well as for RBAC with appropriate permissions and without them.
