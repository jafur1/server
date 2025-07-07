import pytest


class TestProfile:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        # Register and login before each test
        api_client.register_user("profile@test.com", "profilepass", 40)
        api_client.login("profile@test.com", "profilepass")

    def test_get_profile(self, api_client):
        response = api_client.get_profile()
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Neko"  # Default name
        assert "avatar" in data
        assert "status" in data

    def test_update_profile(self, api_client):
        new_name = "Updated Name"
        response = api_client.update_profile(new_name)
        assert response.status_code == 200

        # Verify update
        get_response = api_client.get_profile()
        assert get_response.json()["name"] == new_name

    def test_profile_status_by_age(self, api_client):
        # Test for young cat
        api_client.register_user("young@test.com", "pass", 20)
        api_client.login("young@test.com", "pass")
        response = api_client.get_profile()
        assert "Молоденький котик" in response.json()["status"]

        # Test for adult cat
        api_client.register_user("adult@test.com", "pass", 50)
        api_client.login("adult@test.com", "pass")
        response = api_client.get_profile()
        assert "Взрослый котик" in response.json()["status"]