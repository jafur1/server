import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def register_user(self, email, password, age):
        url = f"{self.base_url}/register"
        data = {
            "email": email,
            "password": password,
            "age": age
        }
        return self.session.post(url, json=data)

    def login(self, email, password):
        url = f"{self.base_url}/login"
        data = {
            "email": email,
            "password": password
        }
        return self.session.post(url, json=data)

    def get_profile(self):
        url = f"{self.base_url}/profile"
        return self.session.get(url)

    def update_profile(self, name):
        url = f"{self.base_url}/profile"
        data = {"name": name}
        return self.session.patch(url, json=data)

    def check_shock_status(self, email):
        url = f"{self.base_url}/check-shock"
        params = {"email": email}
        return self.session.get(url, params=params)
