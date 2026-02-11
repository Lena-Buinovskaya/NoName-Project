import requests

base_url = "https://dummyjson.com"

class ApiClient:
    def get_user(self, user_id):
        return requests.get(f"{base_url}/users/{user_id}", timeout=5)

    def login(self, username, password):
        return requests.post(f"{base_url}/auth/login", data={"username": username, "password": password}, timeout=5)

    def get_products(self):
        return requests.get(f"{base_url}/products", timeout=5)


client = ApiClient()
user = client.get_user(1)
login = client.login(username="emilys",
        password="emifdgdfass")
products = client.get_products()
# print(products.json()['products'][:2])
# print(login.status_code)
# print(login.json())
# print(user.json())