from rest_framework.test import APITestCase
from .models import Amenity


class TestAmeneites(APITestCase):
    NAME = "AMENITY NAME"
    DESC = "AMENITY DESC"
    URL = "/api/v1/rooms/amenities"

    def setUp(self):
        Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        res = self.client.get("/api/v1/rooms/")
        data = res.json()
        self.assertEqual(res.status_code, 200, "!200")
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)

    def test_create_amenity(self):
        name = "new amenity"
        desc = "New DEsc"
        res = self.client.post(
            self.URL,
            data={"name": name, "description": desc},
        )
        data = res.json()
        self.assertEqual(res.status_code, 200, "!200")
        self.assertEqual(data["name"], name)
        self.assertEqual(data["description"], desc)


class TestAmenity(APITestCase):
    NAME = "AMENITY NAME"
    DESC = "AMENITY DESC"
    URL = "/api/v1/rooms/amenity"

    def setUp(self):
        Amenity.objects.create(
            name=self.name,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")
        self.assertEqual(response.status_code, 400)

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], self.NAME)

    def test_put_amenitiy(self):
        pass

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1")
        self.assertEqual(response.status_code, 204)
