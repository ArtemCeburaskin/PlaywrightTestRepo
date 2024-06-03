from playwright.sync_api import Page, expect


def test_logout(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/index.html")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="LOGIN").click()

    burger_menu = page.locator(".bm-burger-button")
    burger_menu.click()
    logout_btn = page.get_by_text("Logout")
    logout_btn.click()

    expect(page.get_by_text("Login")).to_be_visible()
