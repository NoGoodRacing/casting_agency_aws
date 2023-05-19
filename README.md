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

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2IxNjVlZjliMjUxOTE1OTM4YzIiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4Mzc4NzcxMywiZXhwIjoxNjgzODczNzEzLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIl19.JoFcaVb3JOQ4RE9y9FYJSA5QJsi9NAWorstlq2tGY9q96rH3vwLWDcgLvRiV0BxrfpOLjL86r0lbdjCDCB3RYVXU2WxUfY4-Gg9T09jU0951v_jCo007CcX97q9YG2YiltL866EdALbcbYbJOWmTL1-rGJzTouv9X-NR_2X4pfCsm0PcjkR56PzijE_U4xGYeoUEJZycWO2WGxPwcFjHu28E5EaRY62jvoDXuvt16hYqbZJjR-1icWC-QE1U3Alyx3et_MY8aD_-yVan_iQa50SqKdjwF0FMlLVj_aox2TAuhsr8QtMT9o3MAcnV2KfWqv_BEKer8k6VGgdO5-Wp4A

casting_director_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2I3ZTc4YjAzZTYxZDZjMjQyOWEiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4Mzc4Nzc3NywiZXhwIjoxNjgzODczNzc3LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.A6h4gmL6LX80XMpnPnYj4hlviuWZ9Ed_8yDlDbHCosqPco-6F7ioyZU4XtiEH07QUlpSJVmm0eh9UomlOUlPRVQ1-eRerJuY8rEuX-EKIYajOjOBc6U8rsemrdi4Sb7BXwZ_fnK1bkMg-aW4DrCubw9EEiYMl3QUppEMqbWiW3akqmN7XNbdU6YUMLcoA7J46Ir_eZ7ZBTXOWLUKetDhl4P3IwJhJbtDpEZ-VFf0PPr9TFtY63miTLE8QbXsCl55AhWXl_qZIp1NnrOIHebL-Wnjhs8ktNfVgQb2i2kxuNRH8VjV8ChwShrVoSQT9tHHammDen_-6KDSpd93lPTf8g

executive_producer_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRlN2M3Yzc4YjAzZTYxZDZjMWVhM2EiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4Mzc4NzgzNSwiZXhwIjoxNjgzODczODM1LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.ZyGyBfNHD1gGPIAHBZ46HK3wSyrqqJ9zZMr2P-VDYhfaXgkRedVp8jTVkYdNbFvfDfPONBuxZfLG9rJr2Qh4KtmjiUjaKJU7JHHMNbhoNQhcelkOiHM2CUpHRBJAlQ4tdeHJQVoZunSleM0Wd0uLE2h21lmJdCvbCSoUvKTau2xBT6LcDDs4Bx3HACL_5pQnG39Wq2y0mxPt6A8cZOG71bxtdhjesBehf8Eny39x2_3bKzjGDLTkD2jo9tJDPGaGWfp1ZJepYt9EXFIqzB5ut15fnN-Bd0No6tpMVk_bFNIoStgDFTQRIss7s_NgMCTt64A14hmtBzoXVM-IVII5Mw




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
