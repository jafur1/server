import pytest


class TestShock:
    def test_check_shock_status_registered(self, api_client):
        # Register a user first
        email = "shock@test.com"
        api_client.register_user(email, "shockpass", 35)

        # Check shock status
        response = api_client.check_shock_status(email)
        assert response.status_code == 200
        assert response.json()["status"] == "registered"
        assert "Ты уже в ШОКе" in response.json()["message"]

    def test_check_shock_status_not_registered(self, api_client):
        response = api_client.check_shock_status("notregistered@test.com")
        assert response.status_code == 200
        assert response.json()["status"] == "not_registered"
        assert "Ты ещё не в ШОКе" in response.json()["message"]

    def test_check_shock_invalid_email(self, api_client):
        response = api_client.check_shock_status("invalid-email")
        assert response.status_code == 400