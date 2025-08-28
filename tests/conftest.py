import pytest


@pytest.fixture(scope="session")
def base_url(request) -> str:
    """
    Retrieves the `--base-url` value provided via the pytest command-line.

    Ensures that the `--base-url` argument is passed; otherwise, raises an error.

    Args:
        request (pytest.FixtureRequest): The pytest request object to access command-line options.

    Returns:
        str: The base URL of the application as provided via `--base-url`.

    Raises:
        pytest.UsageError: If the `--base-url` argument is missing.
    """
    base_url = request.config.getoption("--base-url")
    if not base_url:
        raise pytest.UsageError(
            "--base-url is missing. It is a required argument. "
            "Please provide it using --base-url=<URL>."
        )
    return base_url


@pytest.fixture(scope="session")
def api_url(base_url: str) -> str:
    """
    Fixture to create the API base URL for tests.

    Args:
        base_url (str): The base URL of the application, typically passed
                        as a pytest command-line argument (`--base-url`).

    Returns:
        str: The full API base URL including the `/rest` endpoint.
    """
    return f"{base_url}/rest"
