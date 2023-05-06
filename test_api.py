import unittest
from fastapi.testclient import TestClient
from main import app, MyDatabase

client = TestClient(app)


class TestApi(unittest.TestCase):
    def test_valid_select_bike(self):
        response = client.get("/Select_bike?id=1")
        print(response.status_code)
        print(response.content)
        print(response.json())

    def test_invalid_select_bike(self):
        response = client.get("/Select_bike?id=100")
        self.assertEqual(response.status_code, 404)

    def test_get_all_bikes(self):
        response = client.get("/All_Bikes")
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        assert "bikes" in response_data
        assert isinstance(response_data["bikes"], list)

    def test_valid_insert_bike(self):
        response = client.post("/Insert_bike",
                               json={"id": 300, "name": "Bike3", "cc": 125, "color": "Blue", "price": 250})
        self.assertEqual(response.status_code, 422)

    def test_invalid_insert_bike(self):
        response = client.post("/Insert_bike",
                               json={"id": "300", "name": "Bike3", "cc": "125", "color": "Blue", "price": "250"})
        self.assertEqual(response.status_code, 422)
        self.assertTrue(True)

    def test_valid_update_bike(self):
        response = client.put("/Update_bike", json={"id": 1, "price": 300})
        self.assertEqual(response.status_code, 422)

    def test_invalid_update_bike(self):
        response = client.put("/Update_bike", json={"id": "1", "price": "300"})
        self.assertEqual(response.status_code, 422)
        self.assertTrue(True)

    def test_valid_delete_bike(self):
        response = client.delete("/Delete_bike?id=1")
        self.assertEqual(response.status_code, 200)

    def test_invalid_delete_bike(self):
        response = client.delete("/Delete_bike?id=200")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(True)
