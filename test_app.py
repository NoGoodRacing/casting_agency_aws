import os
import unittest
import json
from dotenv import load_dotenv
from app import create_app
from models import db, Actor, Movie

load_dotenv()

TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
casting_assistant_jwt = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2IxNjVlZjliMjUxOTE1OTM4YzIiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzcwNjg4NSwiZXhwIjoxNjgzNzkyODg1LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIl19.buJJNT2cIuHyccM27TKhVmixRw-Cci52CYzIo1MQEq9NCDS1xPnpdhDexkvy1BdI8UPnm-c5yqGhkTMHVEiyW16PyHLr2W_2hkTNb3jMQQDBsxXGqtXoq_7jyAsfT9tz4JKRM1KUqzOx5s-q1tn2Xy9BZ0pZ0lMfc3Y0FLzcpSi2e_TtC14HTwnVnbX78gQhF6I4OW7guWhisJGk1d6cvwx6TJBkC6ur6fK_RoCBDckaMsK65njhP5oCkxzdphvjOy_Agiam-zwBcthQl3iVlJdO7Scfxp7cKyX1SaSCOSBobyFTgjqQCoxmcphoT7iVUzPCei2ZBHDSBXDfpMPSyg")
casting_director_jwt = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2I3ZTc4YjAzZTYxZDZjMjQyOWEiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzcwNzUxMCwiZXhwIjoxNjgzNzkzNTEwLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.QVnm5GUPdPajVkOHYXU2ioigHLFVyZPwLhPs8bZqxD7lU3m43CCfEfXNqFi0st7ZxhE56plPaCC8EySdEcejNFuDv2qSooDaVQIg_xJtwACAsP2kMC5ZyiqSsjDfRgjUcdOHECDarfzhiGB1QWvTD9KTGwRoBVGXBeMt_O7nzJVVZK_bG_I07tRdQMNzFuokNKlhNE_M9SV-kXOmEuOzOXFUFDNh0tDh0bTXyFXP4zdiitjlKcwRWeldnwlCD3fhMQG3juhZWsopHZ_IUMEs5a2FBq4DRzfMsLAlT50nlePhIvHVYVNgU7W3fwqBHaHhnfrQcSwyDc6jDHTFN5M01w")
executive_producer_jwt = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRlN2M3Yzc4YjAzZTYxZDZjMWVhM2EiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4MzcwMzM3MSwiZXhwIjoxNjgzNzg5MzcxLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.2E0QtmmQlA2gNL1dnRDok2LHb77SQefEHTh_COaKpIJUYBwIsxpS3ssZpHG0Aeo_4R5vwIxZ0C7VR0-wN3HCpdiANktEe_ewGR15nGPo3nNKytmHojnAu7wjeT6PqeUSjnEhzrKXcwyfdaxpWB8M0LqU6CLpO2JCITFzDgsLP2FF_5ikfC_Aa8NRFIv_tnyFE5B_HNXxHK8-AVa2ZhcIzBgLwd_RXX6WnqlvufSsVulg7BfMd54AtnnfZkSrx6u1Ijuf2Fku35FhmVHj90pmV_oh0cnieQZoKjYDsBmKp48NaXCbNPwEtlNVtOyfnSInVEzA3fmvIapIPJ0ztrr2mw")


class CastingAgency(unittest.TestCase):
    """This class represents the Casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(TEST_DATABASE_URI)
        self.client = self.app.test_client

        self.new_movie = {
            "title": "Fight club",
            "release_date": 1999
        }
        self.new_actor = {
            "name": "Angelina Jolie",
            "age": 47,
            "gender": "F"
        }

    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
            # db.session.rollback()
            pass

    def test_get_movies(self):
        """Testing getting movies from /movies"""
        res = self.client().get("/movies",
                                headers={
                                    "Authorization":
                                        "Bearer " + casting_assistant_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_401_get_movies_without_authorization(self):
        """Testing getting movies from /movies without authorization"""
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"],
                         "Authorization header is expected")

    def test_get_movies_by_id(self):
        """Testing getting categories from /movies"""
        res = self.client().get("/movies/1",
                                headers={
                                    "Authorization":
                                        "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie_info"])

    def test_404_get_movies_by_id(self):
        """Testing 404 when movie doesn't exist from /movies"""
        res = self.client().get("/movies/333",
                                headers={
                                    "Authorization":
                                        "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_delete_movie(self):
        """Testing deleting movie by movie_id"""
        res = self.client().delete("/movies/2",
                                   headers={
                                       "Authorization":
                                           "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        with self.app.app_context():
            movie = db.session.get(Movie, 2)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 2)
        self.assertEqual(movie, None)

    def test_422_if_movie_does_not_exist(self):
        """Testing 422 when movie doesn't exist"""
        res = self.client().delete("/movies/333",
                                   headers={
                                       "Authorization":
                                           "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_401_delete_movies_without_permissions(self):
        """Testing 401 deleting movie from /movies without permissions"""
        res = self.client().delete(
            "/movies/1",
            headers={"Authorization": "Bearer " + casting_director_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"],
                         "Permission not found.")

    def test_create_new_movie(self):
        """Testing creating a new movie"""
        res = self.client().post(
            "/movies",
            json=self.new_movie,
            headers={"Authorization": "Bearer " + executive_producer_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])

    def test_400_for_bad_movie_param(self):
        """Testing 400 with bad movie params"""
        res = self.client().post(
            "/movies",
            json={},
            headers={"Authorization": "Bearer " + executive_producer_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_edit_movie(self):
        """Testing editing movie"""
        res = self.client().patch(
            "/movies/1",
            json=self.new_movie,
            headers={"Authorization": "Bearer " + executive_producer_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])

    def test_404_edit_nonexistent_movie(self):
        """Testing 404 nonexistent movie"""
        res = self.client().patch(
            "/movies/333",
            json=self.new_movie,
            headers={"Authorization": "Bearer " + executive_producer_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # ----------------------------------------------------------------------------
    def test_get_actors(self):
        """Testing getting movies from /movies"""
        res = self.client().get("/actors",
                                headers={
                                    "Authorization":
                                        "Bearer " + casting_assistant_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_401_get_actors_without_authorization(self):
        """Testing getting actors from /actors without authorization"""
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"],
                         "Authorization header is expected")

    def test_get_actors_by_id(self):
        """Testing getting categories from /actors"""
        res = self.client().get("/actors/1",
                                headers={
                                    "Authorization":
                                        "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor_info"])

    def test_404_get_actors_by_id(self):
        """Testing 404 when actor doesn't exist from /actors"""
        res = self.client().get("/actors/333",
                                headers={
                                    "Authorization":
                                        "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_delete_actor(self):
        """Testing deleting actor by actor_id"""
        res = self.client().delete("/actors/2",
                                   headers={
                                       "Authorization":
                                           "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        with self.app.app_context():
            movie = db.session.get(Actor, 2)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 2)
        self.assertEqual(movie, None)

    def test_422_if_actor_does_not_exist(self):
        """Testing 422 when actor doesn't exist"""
        res = self.client().delete("/actors/333",
                                   headers={
                                       "Authorization":
                                           "Bearer " + executive_producer_jwt})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_401_delete_actors_without_permissions(self):
        """Testing 401 deleting actor from /actors without permissions"""
        res = self.client().delete(
            "/actors/1",
            headers={"Authorization": "Bearer " + casting_assistant_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"],
                         "Permission not found.")

    def test_create_new_actor(self):
        """Testing creating a new actor"""
        res = self.client().post(
            "/actors",
            json=self.new_actor,
            headers={"Authorization": "Bearer " + casting_director_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_400_for_bad_actor_param(self):
        """Testing 400 with bad actor params"""
        res = self.client().post(
            "/actors",
            json={},
            headers={"Authorization": "Bearer " + casting_director_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_edit_actor(self):
        """Testing editing actor"""
        res = self.client().patch(
            "/actors/1",
            json=self.new_actor,
            headers={"Authorization": "Bearer " + casting_director_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_404_edit_nonexistent_actor(self):
        """Testing 404 nonexistent actor"""
        res = self.client().patch(
            "/actors/333",
            json=self.new_movie,
            headers={"Authorization": "Bearer " + casting_director_jwt}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
