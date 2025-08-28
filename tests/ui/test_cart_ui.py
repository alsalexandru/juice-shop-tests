from playwright.sync_api import Page


def test_login_valid_ui(page: Page, base_url: str) -> None:
    """
    Test a valid user login through the UI.

    This test navigates to the application's login page, enters valid login credentials,
    and verifies that the user is greeted with a welcome message upon successful login.

    Args:
        page (Page): Playwright page object used for browser automation.
        base_url (str): The base URL of the application.

    Assertions:
        - Checks that the welcome message is visible on the page after a successful login.
    """
    page.goto(base_url)
    page.click("button[aria-label='Go to login page']")
    page.click("button[aria-label='Close Welcome Banner']")
    page.fill("input#email", "admin@juice-sh.op")
    page.fill("input#password", "admin123")
    page.click("button#loginButton")
    assert "Welcome" in page.inner_text("mat-card"), "Expected a welcome message after successful login."


def test_login_invalid_ui(page: Page, base_url: str) -> None:
    """
    Test an invalid user login through the UI.

    This test navigates directly to the application's login page, enters invalid credentials,
    and verifies that an error message is displayed upon login failure.

    Args:
        page (Page): Playwright page object used for browser automation.
        base_url (str): The base URL of the application.

    Assertions:
        - Checks that the UI displays an error message: 'Invalid email or password'.
    """
    page.goto(base_url + "/#/login")
    page.click("button[aria-label='Close Welcome Banner']")
    page.fill("input#email", "wrong@juice-sh.op")
    page.fill("input#password", "badpass")
    page.click("button#loginButton")
    assert "Invalid email or password" in page.inner_text("mat-error"), \
        "Expected error message for invalid login credentials."


def test_add_to_cart_ui(page: Page, base_url: str) -> None:
    """
    Test adding an item to the cart through the UI.

    This test navigates to the application's main page, interacts with the 'Add to cart' button
    for a product, and validates that the cart's item count is incremented.

    Args:
        page (Page): Playwright page object used for browser automation.
        base_url (str): The base URL of the application.

    Assertions:
        - Checks that the value in the basket badge (`<span#basked-badge>`) increases,
          indicating an item was successfully added to the cart.
    """
    page.goto(base_url)
    page.click("button[aria-label='Close Welcome Banner']")
    page.click("button[aria-label='Show/hide basked']")
    page.click("button[aria-label='Add to basked']")

    basked_text: str = page.inner_text("span#basked-badge")
    assert int(basked_text) > 0, "Basket count should increment after adding an item."
