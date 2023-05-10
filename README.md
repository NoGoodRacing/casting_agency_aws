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

Python 3.9

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

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2IxNjVlZjliMjUxOTE1OTM4YzIiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzcwNjg4NSwiZXhwIjoxNjgzNzkyODg1LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIl19.buJJNT2cIuHyccM27TKhVmixRw-Cci52CYzIo1MQEq9NCDS1xPnpdhDexkvy1BdI8UPnm-c5yqGhkTMHVEiyW16PyHLr2W_2hkTNb3jMQQDBsxXGqtXoq_7jyAsfT9tz4JKRM1KUqzOx5s-q1tn2Xy9BZ0pZ0lMfc3Y0FLzcpSi2e_TtC14HTwnVnbX78gQhF6I4OW7guWhisJGk1d6cvwx6TJBkC6ur6fK_RoCBDckaMsK65njhP5oCkxzdphvjOy_Agiam-zwBcthQl3iVlJdO7Scfxp7cKyX1SaSCOSBobyFTgjqQCoxmcphoT7iVUzPCei2ZBHDSBXDfpMPSyg

casting_director_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2I3ZTc4YjAzZTYxZDZjMjQyOWEiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzcwNzUxMCwiZXhwIjoxNjgzNzkzNTEwLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.QVnm5GUPdPajVkOHYXU2ioigHLFVyZPwLhPs8bZqxD7lU3m43CCfEfXNqFi0st7ZxhE56plPaCC8EySdEcejNFuDv2qSooDaVQIg_xJtwACAsP2kMC5ZyiqSsjDfRgjUcdOHECDarfzhiGB1QWvTD9KTGwRoBVGXBeMt_O7nzJVVZK_bG_I07tRdQMNzFuokNKlhNE_M9SV-kXOmEuOzOXFUFDNh0tDh0bTXyFXP4zdiitjlKcwRWeldnwlCD3fhMQG3juhZWsopHZ_IUMEs5a2FBq4DRzfMsLAlT50nlePhIvHVYVNgU7W3fwqBHaHhnfrQcSwyDc6jDHTFN5M01w

executive_producer_jwt:

    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRlN2M3Yzc4YjAzZTYxZDZjMWVhM2EiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzcwMzM3MSwiZXhwIjoxNjgzNzg5MzcxLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.2E0QtmmQlA2gNL1dnRDok2LHb77SQefEHTh_COaKpIJUYBwIsxpS3ssZpHG0Aeo_4R5vwIxZ0C7VR0-wN3HCpdiANktEe_ewGR15nGPo3nNKytmHojnAu7wjeT6PqeUSjnEhzrKXcwyfdaxpWB8M0LqU6CLpO2JCITFzDgsLP2FF_5ikfC_Aa8NRFIv_tnyFE5B_HNXxHK8-AVa2ZhcIzBgLwd_RXX6WnqlvufSsVulg7BfMd54AtnnfZkSrx6u1Ijuf2Fku35FhmVHj90pmV_oh0cnieQZoKjYDsBmKp48NaXCbNPwEtlNVtOyfnSInVEzA3fmvIapIPJ0ztrr2mw




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
