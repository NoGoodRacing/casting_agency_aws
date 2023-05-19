import os
import unittest
import json
from dotenv import load_dotenv
from app import create_app
from models import db, Actor, Movie

load_dotenv()

TEST_DATABASE_URI = os.getenv("TEST_DATABASE_URI")
casting_assistant_jwt = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2IxNjVlZjliMjUxOTE1OTM4YzIiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4Mzc4NzcxMywiZXhwIjoxNjgzODczNzEzLCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIl19.JoFcaVb3JOQ4RE9y9FYJSA5QJsi9NAWorstlq2tGY9q96rH3vwLWDcgLvRiV0BxrfpOLjL86r0lbdjCDCB3RYVXU2WxUfY4-Gg9T09jU0951v_jCo007CcX97q9YG2YiltL866EdALbcbYbJOWmTL1-rGJzTouv9X-NR_2X4pfCsm0PcjkR56PzijE_U4xGYeoUEJZycWO2WGxPwcFjHu28E5EaRY62jvoDXuvt16hYqbZJjR-1icWC-QE1U3Alyx3et_MY8aD_-yVan_iQa50SqKdjwF0FMlLVj_aox2TAuhsr8QtMT9o3MAcnV2KfWqv_BEKer8k6VGgdO5-Wp4A")
casting_director_jwt = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDUwY2I3ZTc4YjAzZTYxZDZjMjQyOWEiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4Mzc4Nzc3NywiZXhwIjoxNjgzODczNzc3LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.A6h4gmL6LX80XMpnPnYj4hlviuWZ9Ed_8yDlDbHCosqPco-6F7ioyZU4XtiEH07QUlpSJVmm0eh9UomlOUlPRVQ1-eRerJuY8rEuX-EKIYajOjOBc6U8rsemrdi4Sb7BXwZ_fnK1bkMg-aW4DrCubw9EEiYMl3QUppEMqbWiW3akqmN7XNbdU6YUMLcoA7J46Ir_eZ7ZBTXOWLUKetDhl4P3IwJhJbtDpEZ-VFf0PPr9TFtY63miTLE8QbXsCl55AhWXl_qZIp1NnrOIHebL-Wnjhs8ktNfVgQb2i2kxuNRH8VjV8ChwShrVoSQT9tHHammDen_-6KDSpd93lPTf8g")
executive_producer_jwt = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZYNGg1YkFnOWxqWHFuX2IwOFREUCJ9.eyJpc3MiOiJodHRwczovL2Rldi1tMW1wb3FyNW90bXJoM3MzLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDRlN2M3Yzc4YjAzZTYxZDZjMWVhM2EiLCJhdWQiOiJjYXN0aW5nX2FnZW5jeSIsImlhdCI6MTY4Mzc4NzgzNSwiZXhwIjoxNjgzODczODM1LCJhenAiOiJxSGNZdFhkTTNOdnJRRzE2eGR5MUZwdGdiZjJTSUs2TSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.ZyGyBfNHD1gGPIAHBZ46HK3wSyrqqJ9zZMr2P-VDYhfaXgkRedVp8jTVkYdNbFvfDfPONBuxZfLG9rJr2Qh4KtmjiUjaKJU7JHHMNbhoNQhcelkOiHM2CUpHRBJAlQ4tdeHJQVoZunSleM0Wd0uLE2h21lmJdCvbCSoUvKTau2xBT6LcDDs4Bx3HACL_5pQnG39Wq2y0mxPt6A8cZOG71bxtdhjesBehf8Eny39x2_3bKzjGDLTkD2jo9tJDPGaGWfp1ZJepYt9EXFIqzB5ut15fnN-Bd0No6tpMVk_bFNIoStgDFTQRIss7s_NgMCTt64A14hmtBzoXVM-IVII5Mw")


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
