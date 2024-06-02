import re
from playwright.sync_api import Page, expect


def test_login_with_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/index.html")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()

    products_header = page.locator(".product_label")
    expect(products_header).to_have_text("Products")


def test_login_with_non_existing_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/index.html")
    page.get_by_placeholder("Username").fill("random")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()

    error_msg = ("Epic sadface: Username and password"
                 " do not match any user in this service")
    error_msg_loc = page.locator("h3[data-test='error']")
    expect(error_msg_loc).to_have_text(error_msg)


def test_login_with_no_credentials(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/index.html")
    page.get_by_role("button", name="LOGIN").click()
    error_msg = "Epic sadface: Username is required"
    error_msg_loc = page.locator("h3[data-test='error']")
    expect(error_msg_loc).to_have_text(error_msg)
