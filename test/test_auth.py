import pytest


class TestAuth:
    def test_register_success(self, api_client):
        email = "test@example.com"
        password = "password123"
        age = 25

        response = api_client.register_user(email, password, age)
        assert response.status_code == 201
        assert "token" in response.json()

    def test_register_invalid_email(self, api_client):
        response = api_client.register_user("invalid", "pass", 20)
        assert response.status_code == 400

    def test_login_success(self, api_client):
        # First register
        api_client.register_user("login@test.com", "pass123", 30)

        # Then login
        response = api_client.login("login@test.com", "pass123")
        assert response.status_code == 200
        assert "token" in response.json()

    def test_login_wrong_password(self, api_client):
        api_client.register_user("wrongpass@test.com", "correct", 25)
        response = api_client.login("wrongpass@test.com", "incorrect")
        assert response.status_code == 401