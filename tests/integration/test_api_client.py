import pytest
from src.api.api_client import ApiClient


@pytest.mark.integration
@pytest.mark.parametrize('field, expected_type', [
    ('id', int),
    ('email', str),
    ('username', str),
    ('password', str),
    ('firstName', str),
    ('lastName', str),
    ('age', int),
    ('gender', str),
    ('phone', str),
    ('address', dict),

])
def test_get_user(field, expected_type):
    api_client = ApiClient()
    user = api_client.get_user(1)

    assert user.status_code == 200

    data = user.json()
    assert field in data
    assert isinstance(data[field], expected_type)


@pytest.mark.integration
def test_get_user_not_found():
    api_client = ApiClient()
    user = api_client.get_user(1000)
    assert user.status_code == 404


@pytest.mark.integration
def test_user_login_success():
    client = ApiClient()

    user_login = client.login('emilys', 'emilyspass')
    assert user_login.status_code == 200

    data = user_login.json()
    assert 'accessToken' in data
    assert 'refreshToken' in data
    assert data['username'] == 'emilys'


@pytest.mark.integration
def test_user_login_failure():
    client = ApiClient()
    user_login = client.login('emilys', 'wrongpass')

    assert user_login.status_code == 400
    assert 'message' in user_login.json()


@pytest.mark.integration
@pytest.mark.parametrize('field, expected_type', [
    ('id', int),
    ('title', str),
    ('description', str),
    ('category', str),
    ('price', float),
    ('rating', float),
    ('tags', list)
])
def test_get_products(field, expected_type):
    client = ApiClient()
    products = client.get_products()

    assert products.status_code == 200
    data = products.json()
    assert 'products' in data

    product = data['products'][0]
    assert field in product
    assert isinstance(product[field], expected_type)