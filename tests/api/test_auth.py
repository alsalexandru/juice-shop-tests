import requests


def test_login_valid(api_url: str) -> None:
    """
    Test that valid user credentials successfully authenticate.

    Args:
        api_url (str): The base URL of the application API.

    Assertions:
        - The status code of the response should be 200.
        - The response JSON should have a key `authentication`.
    """
    r: requests.Response = requests.post(
        f"{api_url}/user/login",
        json={"email": "admin@juice-sh.op", "password": "admin123"},
    )

    assert r.status_code == 200, "Expected status code to be 200 for valid login."
    assert "authentication" in r.json(), "Authentication key should exist in response JSON."


def test_login_invalid(api_url: str) -> None:
    """
    Test that invalid user credentials result in failed authentication.

    Args:
        api_url (str): The base URL of the application API.

    Assertions:
        - The status code of the response should be 401 (Unauthorized).
    """
    r: requests.Response = requests.post(
        f"{api_url}/user/login",
        json={"email": "wrong@juice-sh.op", "password": "badpass"},
    )

    assert r.status_code == 401, "Expected status code to be 401 for invalid login."
